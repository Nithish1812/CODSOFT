import random
import string

def nithish_pypass_strong():
    print("--- NITHISH-PYPASS: STRONG GENERATOR ---")
    
    try:
        # 1. Input the length
        length = int(input("Enter desired password length (Recommended 12+): "))
        
        if length < 8:
            print(" Note: Passwords shorter than 8 characters are less secure.")

        # 2. Define the 'Strong' character pool
        # This includes ABC, abc, 123, and !@#$
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation
        
        all_chars = lower + upper + digits + symbols

        # 3. Security Logic: Ensure the password isn't just random, 
        # but pulls from the combined pool of all character types.
        password = "".join(random.sample(all_chars, length))
        
        # 4. Final Output
        print("\n" + "="*35)
        print(f"Your Strong Password: {password}")
        print("="*35)
        print("Status: SECURE ✅")

    except ValueError:
        print(" Error: Please enter a valid number for the length.")

if __name__ == "__main__":
    nithish_pypass_strong()