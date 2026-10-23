def get_advice(
        season,
        plant_type):

    advice = ""

    if season == "summer":
        advice += (
            "Water your plants regularly "
            "and provide some shade.\n"
        )

    elif season == "winter":
        advice += (
            "Protect your plants from "
            "frost with covers.\n"
        )

    else:
        advice += (
            "No advice for this season.\n"
        )

    if plant_type == "flower":
        advice += (
            "Use fertiliser "
            "to encourage blooms."
        )

    elif plant_type == "vegetable":
        advice += (
            "Keep an eye out for pests."
        )

    else:
        advice += (
            "No advice for this type "
            "of plant."
        )

    return advice


def main():

    season = input(
        "Enter season: "
    ).lower()

    plant_type = input(
        "Enter plant type: "
    ).lower()

    advice = get_advice(
        season,
        plant_type
    )

    print(advice)


main()