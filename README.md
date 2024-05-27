# 🤖 ForestBot
Welcome to the official repository of ForestBot, a specialized chatbot component designed for the ForestQB project. This bot is tailored to enhance user interactions by seamlessly integrating conversational AI with a graphical user interface (GUI), optimizing the data extraction and management process.

## Main Project
For more details about the Forest Query Builder project, please visit the main repository:
- [ForestQB Main Repository](https://github.com/i3omar/ForestQB)

## Installation

To get ForestBot up and running, follow these steps:

```bash
git clone https://github.com/i3omar/ForestBot.git
cd ForestBot
pip install -r requirements.txt
```

## Usage
### Running the Model
After installation, you can run the Rasa server using the pre-trained model:

```bash
rasa run --model models/20230204-004916-soft-angle.tar.gz
```

To run custom actions, execute:

```bash
rasa run actions
```

## Contributing

Contributions to ForestBot are welcome! Please fork the repo, create your feature branch, commit your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Additional Resources

For more details about the ForestQB project, please refer to the [ForestQB main repository](https://github.com/i3omar/ForestQB).
