// Write a C++ program to delete an element in a Singly Linked List 
// (i) at first 
// (ii) at Last 
// (iii) before a key element
// (iv) After a key element

#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
};

Node* createNode(int value) {
    Node* newNode = new Node();
    newNode->data = value;
    newNode->next = nullptr;
    return newNode;
}

void display(Node* head) {
    Node* temp = head;
    while (temp != nullptr) {
        cout << temp->data << " -> ";
        temp = temp->next;
    }
    cout << "NULL" << endl;
}

void insertAtEnd(Node*& head, int value) {
    Node* newNode = createNode(value);
    if (head == nullptr) {
        head = newNode;
        return;
    }
    Node* temp = head;
    while (temp->next != nullptr)
        temp = temp->next;
    temp->next = newNode;
}

void deleteAtBeginning(Node*& head) {
    if (head == nullptr) {
        cout << "List is empty.\n";
        return;
    }
    Node* temp = head;
    head = head->next;
    cout << "Deleted: " << temp->data << endl;
    delete temp;
}

void deleteAtEnd(Node*& head) {
    if (head == nullptr) {
        cout << "List is empty.\n";
        return;
    }

    if (head->next == nullptr) {
        cout << "Deleted: " << head->data << endl;
        delete head;
        head = nullptr;
        return;
    }

    Node* temp = head;
    while (temp->next->next != nullptr)
        temp = temp->next;

    cout << "Deleted: " << temp->next->data << endl;
    delete temp->next;
    temp->next = nullptr;
}

void deleteBeforeKey(Node*& head, int key) {
    if (head == nullptr || head->next == nullptr) {
        cout << "List too short to perform deletion.\n";
        return;
    }

    if (head->data == key) {
        cout << "No node exists before key " << key << ".\n";
        return;
    }

    Node* prev = nullptr;
    Node* curr = head;

    while (curr->next != nullptr && curr->next->data != key) {
        prev = curr;
        curr = curr->next;
    }

    if (curr->next == nullptr) {
        cout << "Key " << key << " not found in list.\n";
        return;
    }

    if (prev == nullptr) {
        head = head->next;
        cout << "Deleted: " << curr->data << endl;
        delete curr;
    } else {
        prev->next = curr->next;
        cout << "Deleted: " << curr->data << endl;
        delete curr;
    }
}

void deleteAfterKey(Node*& head, int key) {
    if (head == nullptr) {
        cout << "List is empty.\n";
        return;
    }

    Node* temp = head;

    while (temp != nullptr && temp->data != key)
        temp = temp->next;

    if (temp == nullptr) {
        cout << "Key " << key << " not found in list.\n";
        return;
    }

    if (temp->next == nullptr) {
        cout << "No node exists after key " << key << ".\n";
        return;
    }

    Node* nodeToDelete = temp->next;
    temp->next = nodeToDelete->next;

    cout << "Deleted: " << nodeToDelete->data << endl;
    delete nodeToDelete;
}

int main() {
    Node* head = nullptr;

    insertAtEnd(head, 10);
    insertAtEnd(head, 20);
    insertAtEnd(head, 30);
    insertAtEnd(head, 40);
    insertAtEnd(head, 50);

    cout << "Initial Linked List:\n";
    display(head);

    cout << "\nDeleting first node:\n";
    deleteAtBeginning(head);
    display(head);
    
    cout << "\nDeleting last node:\n";
    deleteAtEnd(head);
    display(head);

    cout << "\nDeleting node before key 40:\n";
    deleteBeforeKey(head, 40);
    display(head);

    cout << "\nDeleting node after key 20:\n";
    deleteAfterKey(head, 20);
    display(head);

    return 0;
}
