import bottle


@bottle.route("/")
def index():
    return "hello k8s!!"


def main():
    bottle.run(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
