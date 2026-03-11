import streamlit as st

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(page_title="HDFC Bank", page_icon="🏦", layout="wide")

# -------------------------
# CUSTOM CSS
# -------------------------
st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

.title {
    text-align:center;
    font-size:40px;
    font-weight:bold;
    color:#003366;
}

.card {
    padding:20px;
    border-radius:15px;
    background-color:white;
    box-shadow:0px 4px 15px rgba(0,0,0,0.1);
}

.balance-card {
    padding:30px;
    border-radius:20px;
    background:linear-gradient(135deg,#1f77b4,#4facfe);
    color:white;
    text-align:center;
    font-size:25px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# BANK CLASS
# -------------------------
class BankAccount:
    bank_name = "HDFC"

    def __init__(self,name,age,mobile_number,account_no,balance):
        self.name = name
        self.age = age
        self.mobile_number = mobile_number
        self.account_no = account_no
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        return self.balance

    def withdraw(self,amount):
        if amount > self.balance:
            return None
        self.balance -= amount
        return self.balance

    def update_mobile(self,new_mobile):
        self.mobile_number = new_mobile

    def check_balance(self):
        return self.balance


# -------------------------
# SESSION
# -------------------------
if "account" not in st.session_state:
    st.session_state.account = None


# -------------------------
# TITLE
# -------------------------
st.markdown('<p class="title">🏦 HDFC Bank Application</p>', unsafe_allow_html=True)


# -------------------------
# SIDEBAR
# -------------------------
menu = st.sidebar.radio(
    "📌 Menu",
    ["Create Account","Deposit","Withdraw","Check Balance","Update Mobile"]
)

# -------------------------
# CREATE ACCOUNT
# -------------------------
if menu == "Create Account":

    st.subheader("📝 Create New Account")

    col1,col2 = st.columns(2)

    with col1:
        name = st.text_input("Name")
        age = st.number_input("Age",min_value=18)

    with col2:
        mobile = st.text_input("Mobile Number")
        acc_no = st.text_input("Account Number")

    balance = st.number_input("Initial Balance",min_value=0)

    if st.button("Create Account"):

        st.session_state.account = BankAccount(
            name,age,mobile,acc_no,balance
        )

        st.success("✅ Account Created Successfully")


# -------------------------
# DEPOSIT
# -------------------------
elif menu == "Deposit":

    st.subheader("💰 Deposit Money")

    if st.session_state.account:

        amount = st.number_input("Enter Amount",min_value=1)

        if st.button("Deposit"):

            new_balance = st.session_state.account.deposit(amount)

            st.success(f"💵 Deposit Successful")
            st.info(f"New Balance: {new_balance}")

    else:
        st.warning("⚠ Create an account first")


# -------------------------
# WITHDRAW
# -------------------------
elif menu == "Withdraw":

    st.subheader("💸 Withdraw Money")

    if st.session_state.account:

        amount = st.number_input("Enter Amount",min_value=1)

        if st.button("Withdraw"):

            result = st.session_state.account.withdraw(amount)

            if result == None:
                st.error("❌ Insufficient Balance")

            else:
                st.success("✅ Withdrawal Successful")
                st.info(f"Remaining Balance: {result}")

    else:
        st.warning("⚠ Create an account first")


# -------------------------
# CHECK BALANCE
# -------------------------
elif menu == "Check Balance":

    st.subheader("📊 Account Balance")

    if st.session_state.account:

        balance = st.session_state.account.check_balance()

        st.markdown(f"""
        <div class="balance-card">
        💰 Current Balance <br><br>
        ₹ {balance}
        </div>
        """,unsafe_allow_html=True)

    else:
        st.warning("⚠ Create an account first")


# -------------------------
# UPDATE MOBILE
# -------------------------
elif menu == "Update Mobile":

    st.subheader("📱 Update Mobile Number")

    if st.session_state.account:

        new_mobile = st.text_input("New Mobile Number")

        if st.button("Update"):

            st.session_state.account.update_mobile(new_mobile)

            st.success("✅ Mobile Number Updated")

    else:
        st.warning("⚠ Create an account first")