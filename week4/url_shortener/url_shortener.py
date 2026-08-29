import string
import time

from flask import Flask, jsonify, redirect, request

app = Flask(__name__)

url_store = {}  # code -> original_url
request_counts = {}  # ip -> list of request timestamps

RATE_LIMIT = 5
WINDOW_SECONDS = 60

BASE62 = string.digits + string.ascii_lowercase + string.ascii_uppercase
next_id = 1  # simulates the autoincrementing primary key in a database


def to_base62(num):
    if num < 62:
        return BASE62[num]
    return to_base62(num // 62) + BASE62[num % 62]


def is_rate_limited(ip):
    now = time.time()
    timestamps = [t for t in request_counts.get(ip, []) if now - t < WINDOW_SECONDS]

    if len(timestamps) >= RATE_LIMIT:
        request_counts[ip] = timestamps
        return True

    timestamps.append(now)
    request_counts[ip] = timestamps
    return False


@app.route("/shorten", methods=["POST"])
def shorten():
    if is_rate_limited(request.remote_addr):
        return jsonify({"message": "Too many requests"}), 429

    data = request.get_json()
    original_url = data.get("url") if data else None
    if not original_url:
        return jsonify({"message": "Missing url"}), 400

    global next_id
    code = to_base62(next_id)
    next_id += 1
    url_store[code] = original_url

    return jsonify({"code": code, "short_url": request.host_url + code}), 201


@app.route("/<code>", methods=["GET"])
def resolve(code):
    if is_rate_limited(request.remote_addr):
        return jsonify({"message": "Too many requests"}), 429

    original_url = url_store.get(code)
    if not original_url:
        return jsonify({"message": "Not found"}), 404

    return redirect(original_url)


if __name__ == "__main__":
    app.run(debug=True)
