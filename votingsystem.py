import os
from datetime import datetime
import matplotlib.pyplot as plt

# ---------------- Voter Class ----------------
class Voter:
    def __init__(self, name, vote, time):
        self.name = name
        self.vote = vote
        self.time = time

# ---------------- Voting System ----------------
class VotingSystem:
    def __init__(self, filename="votes.txt"):
        self.filename = filename
        self.votes = {}   # name : (vote, time)
        self.load_votes()

    # -------- File Handling --------
    def load_votes(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                for line in file:
                    name, vote, time = line.strip().split(",")
                    self.votes[name] = (vote, time)

    def save_votes(self):
        with open(self.filename, "w") as file:
            for name, data in self.votes.items():
                file.write(f"{name},{data[0]},{data[1]}\n")

    # -------- CRUD Operations --------
    def add_vote(self):
        name = input("Enter voter name: ").strip()

        if not name:
            print("❌ Name cannot be empty.")
            return

        if name in self.votes:
            print("❌ Fraud Detected! You have already voted.")
            return

        vote = input("Enter vote (Yes/No): ").strip().capitalize()
        if vote not in ["Yes", "No"]:
            print("❌ Invalid vote choice.")
            return

        time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.votes[name] = (vote, time)
        self.save_votes()

        print("✅ Vote recorded successfully.")

    def view_votes(self):
        if not self.votes:
            print("No votes available.")
            return

        print("\n--- All Votes ---")
        for name, data in self.votes.items():
            print(f"Name: {name}, Vote: {data[0]}, Time: {data[1]}")

    def update_vote(self):
        name = input("Enter voter name to update: ").strip()
        if name not in self.votes:
            print("❌ Voter not found.")
            return

        new_vote = input("Enter new vote (Yes/No): ").strip().capitalize()
        if new_vote not in ["Yes", "No"]:
            print("❌ Invalid vote choice.")
            return

        time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.votes[name] = (new_vote, time)
        self.save_votes()

        print("✅ Vote updated successfully.")

    def delete_vote(self):
        name = input("Enter voter name to delete: ").strip()
        if name in self.votes:
            del self.votes[name]
            self.save_votes()
            print("✅ Vote deleted successfully.")
        else:
            print("❌ Voter not found.")

    def search_voter(self):
        name = input("Enter voter name to search: ").strip()
        if name in self.votes:
            vote, time = self.votes[name]
            print(f"Name: {name}, Vote: {vote}, Time: {time}")
        else:
            print("❌ Voter not found.")

    # -------- Results --------
    def show_results(self):
        yes_votes = sum(1 for v in self.votes.values() if v[0] == "Yes")
        no_votes = sum(1 for v in self.votes.values() if v[0] == "No")
        total = len(self.votes)

        print("\n--- Voting Summary ---")
        print(f"Total Voters : {total}")
        print(f"Yes Votes    : {yes_votes}")
        print(f"No Votes     : {no_votes}")

    def show_graph(self):
        yes_votes = sum(1 for v in self.votes.values() if v[0] == "Yes")
        no_votes = sum(1 for v in self.votes.values() if v[0] == "No")

        plt.bar(["Yes", "No"], [yes_votes, no_votes])
        plt.title("Voting Results")
        plt.xlabel("Vote Type")
        plt.ylabel("Number of Votes")
        plt.show()

    def reset_votes(self):
        self.votes.clear()
        self.save_votes()
        print("✅ All votes reset successfully.")

# ---------------- Admin Login ----------------
def admin_login():
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")
    return username == "admin" and password == "admin123"

# ---------------- Main Menu ----------------
def main():
    system = VotingSystem()

    while True:
        print("\n===== VOTING SYSTEM =====")
        print("1. Cast Vote")
        print("2. Admin Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            system.add_vote()

        elif choice == "2":
            if admin_login():
                while True:
                    print("\n--- ADMIN MENU ---")
                    print("1. View All Votes")
                    print("2. Update Vote")
                    print("3. Delete Vote")
                    print("4. Search Voter")
                    print("5. View Results")
                    print("6. View Results Graph")
                    print("7. Reset Voting")
                    print("8. Logout")

                    admin_choice = input("Enter choice: ")

                    if admin_choice == "1":
                        system.view_votes()
                    elif admin_choice == "2":
                        system.update_vote()
                    elif admin_choice == "3":
                        system.delete_vote()
                    elif admin_choice == "4":
                        system.search_voter()
                    elif admin_choice == "5":
                        system.show_results()
                    elif admin_choice == "6":
                        system.show_graph()
                    elif admin_choice == "7":
                        system.reset_votes()
                    elif admin_choice == "8":
                        break
                    else:
                        print("❌ Invalid choice.")
            else:
                print("❌ Invalid admin credentials.")

        elif choice == "3":
            print("Exiting Voting System...")
            break

        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
