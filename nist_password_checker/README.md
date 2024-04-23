This Python script is designed to meet some requirements from the [National Institute of Standards and Technology (NIST) Special Publication 800-63B Digital Identity Guidelines](https://pages.nist.gov/800-63-3/sp800-63b.html#sec5), focusing on the creation and management of memorized secrets (passwords). Here are the key features based on the NIST guidelines:

1. **Minimum Length Requirement**:
    - Passwords must be at least 8 characters long. This aligns with Section 5.1.1 of the guidelines, which states: "Memorized secrets SHALL be at least 8 characters in length if chosen by the subscriber."
    - Encourages users to use longer passwords as suggested in Appendix A.2: "Users should be encouraged to make their passwords as lengthy as they want, within reasonable limits."
2. **Composition Flexibility**:
    - The script accepts all types of characters, including special characters, adhering to the guideline's recommendation against mandatory composition rules (i.e., mixing uppercase, lowercase, numbers, and symbols).
3. **Prohibition of Obvious Passwords**:
    - Checks for repetitive or sequential characters to prevent easily guessable passwords.
    - Compares submitted password against OWASP’s list of 500 worst passwords  obtained from  [OWASP's 500 worst password lis](https://github.com/OWASP/passfault/tree/master/wordlists/wordlists)t to ensure they are not too common or previously compromised. This is based on Section 5.1.1.2: "When processing requests to establish and change memorized secrets, verifiers SHALL compare the prospective secrets against a list that contains values known to be commonly-used, expected, or compromised."


