# Social Justice AI

<img src="./image/banner.png">

Social Justice AI is a Streamlit-based application designed to empower communities by providing localized legal knowledge. By utilizing OpenAI's language model, the app offers users accurate legal information tailored to their specific location.

## Features

- **Location-Based Legal Information:** Automatically detects the user's location and provides relevant legal information.
- **Interactive Chat Interface:** Users can ask legal questions through a chat interface, and receive detailed responses from the AI.
- **User-Friendly Design:** Clean, modern design with custom styling for an enhanced user experience.

## Installation

To run the Social Justice AI app locally, follow these steps:

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/social-justice-ai.git
    cd social-justice-ai
    ```

2. **Install Dependencies:**

    Create a virtual environment and install the required packages:

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    pip install -r requirements.txt
    ```

3. **Set Up Environment Variables:**

    Create a `.env` file in the root directory and add your OpenAI API key:

    ```plaintext
    OPENAI_API_KEY=your_openai_api_key
    ```

4. **Run the App:**

    Start the Streamlit app:

    ```bash
    streamlit run app.py
    ```

## Usage

1. **Open the App:**
    - Navigate to `http://localhost:8501` in your web browser.

2. **Interact with the Chat Interface:**
    - Enter your legal question in the chat input box.
    - The AI will generate and display a response based on your location.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.


## Contributing

We welcome contributions to enhance Social Justice AI. To contribute, follow these steps:

1. **Fork the Repository:**

    ```bash
    git clone https://github.com/DeepeshKalura/social-justice-ai
    cd social-justice-ai
    ```

2. **Create a Branch:**

    ```bash
    git checkout -b feature-branch
    ```

3. **Make Your Changes:**
    - Ensure your code follows the existing code style.
    - Test your changes thoroughly.

4. **Commit and Push:**

    ```bash
    git add .
    git commit -m "Description of changes"
    git push origin feature-branch
    ```

5. **Create a Pull Request:**
    - Go to the repository on GitHub and create a pull request.

## Contact

For any questions or feedback, please reach out to us at [deepeshkalurs@gmail.com](mailto:deepeshkalurs@gmail.com).