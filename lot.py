import streamlit as st

def main():
    st.title("Profit and Loss BankNifty Lot Calculator")
    capital = 3000
    profit_percentage = 10 / 100
    loss_percentage = 5 / 100
    lot = 15
    premium = 1
    selling = 1
    premiumgain = 1
   
    # Input from the user
    input_value = st.number_input("Enter premium (float value): ")
    premium = float(input_value or 1)

    # Calculate total lot
    total_lot = int(capital / premium)
    no_of_lot = int(total_lot / 15)

    # Calculate profit and loss on capital
    profit_on_capital = no_of_lot * 15 * premium * profit_percentage
    loss_on_capital = no_of_lot * 15 * premium * loss_percentage

    # Selling on premium
    selling = ((15 * no_of_lot * premium) + profit_on_capital) / (15 * no_of_lot)
    premiumgain = selling - premium

    # Display the variables
    st.write("Capital:", capital)
    st.write("Lot:", no_of_lot)
    st.write("Premium:", premium)
    st.write("Total qty:", no_of_lot * 15)
    st.write("Profit on Capital:", profit_on_capital)
    st.write("Loss on Capital:", loss_on_capital)
    st.write("Selling on premium:", selling)
    st.write("Total premium gain:", premiumgain)

if __name__ == "__main__":
    main()
