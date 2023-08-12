import sys
import json
import os
import http.client

WLED_IP = os.environ.get("WLED_IP")


# Function to create an Alfred item
def create_alfred_item(title, arg):
    return {"title": title, "arg": arg}


# Function to get the list of effects from WLED
def get_effects():
    try:
        conn = http.client.HTTPConnection(WLED_IP)
        conn.request("GET", "/json/effects")
        response = conn.getresponse()
        if response.status == 200:
            data = response.read()
            return json.loads(data)
        else:
            print(f"Failed to fetch effects. Status code: {response.status}")
            sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    finally:
        conn.close()


def main():
    # Get the list of effects
    effects_list = get_effects()
    search_query = sys.argv[1].lower() if len(sys.argv) > 1 else None

    # Filter the effects based on the user query (if provided)
    if search_query is None:
        effects_list = [
            create_alfred_item(effect, index)
            for index, effect in enumerate(effects_list)
        ]

    else:
        effects_list = [
            create_alfred_item(effect, index)
            for index, effect in enumerate(effects_list)
            if search_query in effect.lower()
        ]

    # Display the list of effects
    output = json.dumps({"items": effects_list})
    print(output)


if __name__ == "__main__":
    main()
