import streamlit as st
import random

def check_length(password, min_length=8):
    return len(password) >= min_length

def has_uppercase(password):
    return any(c.isupper() for c in password)

def has_lowercase(password):
    return any(c.islower() for c in password)

def has_digit(password):
    return any(c.isdigit() for c in password)

def has_special(password, special_chars="!@#$%^&*()-_=+[]{}|;:'\",.<>?/"):
    return any(c in special_chars for c in password)

def password_strength(password):
    checks = {
        "Length (8+)": check_length(password),
        "Uppercase": has_uppercase(password),
        "Lowercase": has_lowercase(password),
        "Digit": has_digit(password),
        "Special Char": has_special(password)
    }

    score = sum(checks.values())

    roast_weak = [
        "Did you type this with your elbows?",
        "Bruh, my grandma could hack that.",
        "That is Shitty as f**k!",
        "Really? Did you even try?",
        "C'mon not your name - retardio.",
        "Your password's so predictable, I guessed it twice."

    ]

    roast_okay = [
        "Decent, but hackers love 'decent'.",
        "Almost there—stop being lazy.",
        "Not bad, but don't celebrate yet.",
        "Better, but still mehn."
    ]

    roast_strong = [
        "Strong password! Where has this been all along?",
        "Finally, a password worth typing!",
        "Noicee! Look's Solid"
    ]

    if score <= 2:
        roast = random.choice(roast_weak)
        message = f"Weak 💩 — {roast}"
    elif score <= 4:
        roast = random.choice(roast_okay)
        message = f"Okay 😐 — {roast}"
    else:
        roast = random.choice(roast_strong)
        message = f"Strong 💪 — {roast}"

    return checks, score, message

# Streamlit App
st.set_page_config(page_title="Smart Password Checker 🔐", page_icon="🔐")
st.title("🔐 Smart Password Strength Meter")

password = st.text_input("Enter your password", type="password")

if password:
    checks, score, message = password_strength(password)

    st.subheader("Password Analysis:")
    for check, passed in checks.items():
        emoji = "✅" if passed else "❌"
        st.write(f"{emoji} **{check}**")

    st.markdown(f"### {message} ({score}/5)")

    if score < 5:
        st.warning("🚨 Improve your password:")
        if not checks["Length (8+)"]:
            st.write("- Make your password at least **8 characters long**.")
        if not checks["Uppercase"]:
            st.write("- Add **uppercase letters** (A-Z).")
        if not checks["Lowercase"]:
            st.write("- Add **lowercase letters** (a-z).")
        if not checks["Digit"]:
            st.write("- Include **numbers** (0-9).")
        if not checks["Special Char"]:
            st.write("- Add **special characters** (e.g., !, @, #, $).")
    else:
        st.success("🎉 Your password looks great!")

    st.info("""
    **💡 Cyber Security Tip:**  
    *Use strong, frequently updated passwords to protect yourself from malware attacks.*
    """)













# password = input("Enter your password: ")

# print("lenght OK?", len(password) >= 8)
# print("Has uppercase?", any(c.isupper() for c in password))
# print("Has lowecase?", any(c.islower() for c in password))
# print("Has digit?", any(c.isdigit() for c in password))
# print("Has special char?", any(c in "!@#$%^&*()" for c in password))

# score = 0

# if len(password) >= 8:
#     score += 1
# if any(c.isupper() for c in password) and any(c.islower() for c in password):
#     score += 1
# if any(c.isdigit() for c in password):
#     score += 1
# if any(c in "!@#$%^&*()" for c in password):
#     score += 1

# if score == 4:
#     message = "Very Strong 🔐"
# elif score == 3:
#     message = "Strong 💪"
# elif score == 2:
#     message = "Okay 😐"
# else:
#     message = "Weak 💩"

# print(f"Score: {score}/4 — {message}")
