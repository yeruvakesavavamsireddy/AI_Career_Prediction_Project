def get_career_role(level, interest, style):
    """
    Determines AI/ML career role based on user inputs.
    """

    if interest == "data":
        if style == "analysis":
            return (
                "Data Scientist",
                "Analyzes structured data to extract insights and build predictive models."
            )
        elif style == "modeling":
            return (
                "Machine Learning Engineer",
                "Builds and deploys scalable ML models for production systems."
            )

    elif interest == "text":
        if style in ["research", "development"]:
            return (
                "NLP Engineer",
                "Designs systems that understand and generate human language."
            )

    elif interest == "images":
        if style in ["modeling", "development"]:
            return (
                "Computer Vision Engineer",
                "Builds models that interpret visual data like images and videos."
            )

    elif interest == "ai systems":
        if level == "advanced":
            return (
                "AI Engineer",
                "Designs end-to-end AI systems integrated into real-world applications."
            )

    return (
        "AI Generalist",
        "Works across multiple AI domains with a broad skill set."
    )


def main():
    print("=== AI Career Profile Generator ===\n")

    level = input(
        "Programming level (Beginner / Intermediate / Advanced): "
    ).strip().lower()

    interest = input(
        "Area of interest (Data / Text / Images / AI Systems): "
    ).strip().lower()

    style = input(
        "Preferred work style (Research / Development / Analysis / Modeling): "
    ).strip().lower()

    role, description = get_career_role(level, interest, style)

    print("\n--- Suggested Career Role ---")
    print(f"Role        : {role}")
    print(f"Description : {description}")


if __name__ == "__main__":
    main()


