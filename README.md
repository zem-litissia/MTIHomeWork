# Association Management – SOLID Refactor

## 🎯 Objective
Refactor the initial club management code using the **5 SOLID principles** to ensure scalability, maintainability, and clean architecture.

---

## ✅ Applied SOLID Principles

### 1. SRP — Single Responsibility Principle
- **Before:** `Member` class handled both data and file operations.
- **After:** Split into:
  - `Member` → stores data.
  - `MemberRepository` → handles loading/saving via `StorageInterface`.

### 2. OCP — Open/Closed Principle
- Extended `Event` into subclasses:
  - `Trip`, `Meeting`, `Competition`.
- Added new `Payable` subclasses:
  - `Donation`, `Subscription`.
- No modification to base logic was needed.

### 3. LSP — Liskov Substitution Principle
- `Trip`, `Meeting`, and `Competition` can replace `Event` seamlessly.
- Function `display_event_details(event)` works with all subclasses.

### 4. ISP — Interface Segregation Principle
- Created small, specific interfaces:
  - `Payable`, `Organizable`, `Registrable`.

### 5. DIP — Dependency Inversion Principle
- High-level classes depend on abstractions, not implementations.
- Example: `MemberRepository` uses `StorageInterface`, allowing `CSVStorage`, `JSONStorage`, or others.

---

## 🗂 Project Structure
