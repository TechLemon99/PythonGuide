import requests
from bs4 import BeautifulSoup

def get_weather(city):
    """Get weather data from Google search for a given city"""
    try:
        # Create URL and request instance
        url = f"https://www.google.com/search?q=weather+{city.replace(' ', '+')}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        
        # Get HTML content
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        html = response.content

        # Parse HTML
        soup = BeautifulSoup(html, 'html.parser')
        
        # Extract temperature - updated class name
        temp_element = soup.find('span', class_='wob_t q8U8x')
        temp = temp_element.text if temp_element else "N/A"
        
        # Extract time and sky description - updated class names
        time_element = soup.find('div', class_='wob_dts')
        sky_element = soup.find('span', class_='wob_dc')
        
        time = time_element.text if time_element else "N/A"
        sky = sky_element.text if sky_element else "N/A"

        # Extract additional weather data - updated class names
        additional_info = soup.find_all('div', class_='wtsRwe')
        other_data = additional_info[0].text if additional_info else "No additional data"

        # Print all weather data
        print(f"\nWeather in {city.title()}:")
        print(f"Temperature: {temp}°C")
        print(f"Time: {time}")
        print(f"Conditions: {sky}")
        print(f"Additional Info: {other_data}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    city = input("Enter city name: ").strip()
    if city:
        get_weather(city)
    else:
        print("Please enter a valid city name")