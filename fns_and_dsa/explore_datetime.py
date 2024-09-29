from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("YYYY-MM-DD HH:MM:SS")

    print(f"Current date and time:{formatted_date}")


def calculate_future_date(days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    formatted_future_date = future_date.strftime("YYYY-MM-DD")
    print(f"Future date:{formatted_future_date}")

def main():
    display_current_datetime()
    try:
        days_to_add = int(input("Enter the number of days to add to the current date:" )) 
        calculate_future_date(days_to_add)
    except ValueError:

       print("Please enter a valid integer for the number of days.")

if __name__ == "__main__":
    main()


