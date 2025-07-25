from agents import function_tool

@function_tool
def get_career_roadmap(career: str) -> str:
    """
    Returns a step-by-step learning roadmap for the specified career path.
    """
    roadmap = {
        "frontend developer": (
            "Start with the basics of HTML, CSS, and JavaScript. "
            "Then advance to modern frameworks like React. "
            "Build real-world projects for your portfolio, and learn version control using Git. "
            "Familiarize yourself with basic testing and debugging tools."
        ),
        "data scientist": (
            "Begin by mastering Python and data libraries such as Pandas and NumPy. "
            "Learn the fundamentals of machine learning and practice on real-world datasets. "
            "Develop SQL skills and gain hands-on experience with data analysis and modeling projects."
        ),
        "graphic designer": (
            "Learn design tools like Adobe Photoshop, Illustrator, and Figma. "
            "Understand the core principles of UI/UX design. "
            "Work on creative projects and build a professional portfolio that showcases your skills."
        ),
        "ai engineer": (
            "Study machine learning and deep learning concepts. "
            "Gain experience with frameworks like TensorFlow and PyTorch. "
            "Work on projects involving natural language processing and AI-based applications."
        ),
    }
    return roadmap.get(career.lower(), "Sorry, no roadmap found for that career field.")
