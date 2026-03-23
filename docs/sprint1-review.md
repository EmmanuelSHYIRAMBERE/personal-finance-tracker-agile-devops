# Sprint 1 Review — Personal Finance Tracker

## Overview

Sprint 1 focused on delivering the core foundation of the Personal Finance Tracker application. The goal was to implement basic account management and transaction handling while establishing a working CI pipeline with automated testing.

---

## Objectives

- Implement core account functionality
- Enable transaction recording (income and expenses)
- Ensure balance updates dynamically
- Set up CI/CD pipeline with automated testing

---

## Features Delivered

### 1. Account Management

- Created an `Account` class to represent user accounts
- Initialized accounts with a starting balance
- Provided methods to retrieve account details

### 2. Transaction Handling

- Implemented support for:
  - Income transactions
  - Expense transactions

- Automatically updated account balance after each transaction
- Stored transaction history for future reporting

### 3. Balance Tracking

- Real-time balance updates after every transaction
- Encapsulation of balance using class methods

### 4. Testing Integration

- Developed unit tests for:
  - Account creation
  - Income transactions
  - Expense transactions

- Integrated tests into CI pipeline using GitHub Actions

### 5. CI/CD Pipeline

- Configured GitHub Actions workflow
- Automated test execution on every push
- Fixed pipeline issues and ensured successful builds

---

## Demo (Evidence)

### Example Output

```
Account created!
Account(Main Account, Balance=1000)

Updated Balance: 1300
```

### CI Pipeline

- All tests passing ✅
- Workflow runs successfully on push

---

## Conclusion

Sprint 1 successfully delivered a working foundation of the Personal Finance Tracker. The system now supports account creation, transaction handling, and automated testing, forming a solid base for further feature development in Sprint 2.
