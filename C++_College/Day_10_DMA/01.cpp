// Write a C++ program to insert an element in a Singly Linked List: 
// (i) at first 
// (ii) at Last 
// (iii) before a key element 
// (iv) after a key element

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

void insertAtBeginning(Node*& head, int value) {
    Node* newNode = createNode(value);
    newNode->next = head;
    head = newNode;
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

void insertBeforeKey(Node*& head, int key, int value) {
    if (head == nullptr) {
        cout << "List is empty.\n";
        return;
    }

    if (head->data == key) {
        insertAtBeginning(head, value);
        return;
    }

    Node* temp = head;
    while (temp->next != nullptr && temp->next->data != key)
        temp = temp->next;

    if (temp->next == nullptr) {
        cout << "Key " << key << " not found in the list.\n";
    } else {
        Node* newNode = createNode(value);
        newNode->next = temp->next;
        temp->next = newNode;
    }
}

void insertAfterKey(Node* head, int key, int value) {
    Node* temp = head;
    while (temp != nullptr && temp->data != key)
        temp = temp->next;

    if (temp == nullptr) {
        cout << "Key " << key << " not found in the list.\n";
    } else {
        Node* newNode = createNode(value);
        newNode->next = temp->next;
        temp->next = newNode;
    }
}

int main() {
    Node* head = nullptr;

    insertAtEnd(head, 10);
    insertAtEnd(head, 20);
    insertAtEnd(head, 30);
    insertAtEnd(head, 40);

    cout << "Initial Linked List: ";
    display(head);

    insertAtBeginning(head, 5);
    cout << "\nAfter inserting 5 at the beginning:\n";
    display(head);

    insertAtEnd(head, 50);
    cout << "\nAfter inserting 50 at the end:\n";
    display(head);

    insertBeforeKey(head, 30, 25);
    cout << "\nAfter inserting 25 before 30:\n";
    display(head);

    insertAfterKey(head, 40, 45);
    cout << "\nAfter inserting 45 after 40:\n";
    display(head);

    return 0;
}
