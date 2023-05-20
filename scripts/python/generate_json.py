import json

def main():
    return_dict = {
        "name": "zach",
        "company": "Red Hat"
    }

    print(json.dumps(return_dict))

if __name__ == "__main__":
    main()