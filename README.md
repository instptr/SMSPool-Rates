# SMSPool-Cheapest-Price

This tool is designed to find the lowest prices for various services across different countries using the SMSPool API. It helps users identify the most cost-effective options available for specific services provided by SMSPool.

## Features

- Retrieve all available services from SMSPool.
- Fetch and list all supported countries.
- Search for specific service IDs.
- Check and compare prices across different countries.
- Display the top three cheapest options for a selected service.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.x
- `requests` library
- `colorama` library

You can install the necessary Python libraries using pip:

\```bash
pip install requests colorama
\```

## Configuration

Set your SMSPool API key in the .env file:

\```
API_KEY=key_here
\```
To get a API KEY go to https://www.smspool.net/my/settings.

## Usage

To run the tool, simply execute the script from your command line:

\```bash
python main.py
\```

Follow the on-screen prompts to enter the service name and view the cheapest prices.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.
