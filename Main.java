import java.util.*;

class User {
    String name;
    int balance;
    int pin;

    User(String name, int balance, int pin) {
        this.name = name;
        this.balance = balance;
        this.pin = pin;
    }
}

class Bank {
    String name;
    Map<String, User> users;

    Bank(String name) {
        this.name = name;
        this.users = new HashMap<>();
    }

    void addUser(User user) {
        users.put(user.name, user);
    }

    User getUser(String name) {
        return users.get(name);
    }
}

class Admin {
    Map<String, Bank> banks;

    Admin() {
        this.banks = new HashMap<>();
    }

    void addBank(Bank bank) {
        banks.put(bank.name, bank);
    }

    Bank getBank(String name) {
        return banks.get(name);
    }
}

public class Main {
    public static void main(String[] args) {
        
        Admin admin = new Admin();
        Bank bank1 = new Bank("KYB");
        Bank bank2 = new Bank("HDFC");
        Bank bank3 = new Bank("ICICI");

        admin.addBank(bank1);
        admin.addBank(bank2);
        admin.addBank(bank3);

        User user1 = new User("User1", 1000, 1234);
        User user2 = new User("User2", 2000, 2345);
        User user3 = new User("User3", 3000, 3456);

        bank1.addUser(user1);
        bank2.addUser(user2);
        bank3.addUser(user3);

        // User selects login account
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter bank name:");
        String bankName = scanner.nextLine();
        System.out.println("Enter user name:");
        String userName = scanner.nextLine();

        Bank selectedBank = admin.getBank(bankName);
        User selectedUser = selectedBank.getUser(userName);

        // User can check balance
        System.out.println(selectedUser.balance);

        // User can deposit money
        selectedUser.balance += 500;
        System.out.println(selectedUser.balance);

        // User can withdraw money
        selectedUser.balance -= 200;
        System.out.println(selectedUser.balance);

        // User can change pin
        selectedUser.pin = 5678;
        System.out.println(selectedUser.pin);

        // Admin can change user balance
        admin.getBank(bankName).getUser(userName).balance = 5000;
        System.out.println(admin.getBank(bankName).getUser(userName).balance);
    }
}