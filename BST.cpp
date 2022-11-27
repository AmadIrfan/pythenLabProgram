#include <iostream>
using namespace std;
// node class
class Node
{
public:
    int data;
    Node *parent;
    Node *left;
    Node *right;
};

// BST Class
class BST
{
private:
    // root node pointer
    Node *root = NULL;

public:
    bool isEmpty()
    {
        return this->root == NULL;
    }
    Node *getTree()
    {
        return root;
    }
    void insert(int x)
    {
        Node *newNode = new Node();
        newNode->data = x;
        newNode->left = NULL;
        newNode->right = NULL;
        if (isEmpty())
        {
            root = newNode;
            newNode->parent = NULL;
        }
        else
        {
            Node *temp = root;
            while (temp != NULL)
            {
                if (x < temp->data)
                {
                    if (temp->left == NULL)
                    {
                        temp->left = newNode;
                        newNode->parent = temp;
                        break;
                    }
                    else
                    {
                        temp = temp->left;
                    }
                }
                else
                {
                    if (temp->right == NULL)
                    {
                        temp->right = newNode;
                        newNode->parent = temp;
                        break;
                    }
                    else
                    {
                        temp = temp->right;
                    }
                }
            }
        }
    }
    void InOrderTraversal(Node *T)
    {
        if (T != NULL)
        {
            InOrderTraversal(T->left);
            cout << T->data << " ";
            InOrderTraversal(T->right);
        }
    }
    void PreOrderTraversal(Node *T)
    {
        if (T != NULL)
        {
            cout << T->data << " ";
            PreOrderTraversal(T->left);
            PreOrderTraversal(T->right);
        }
    }
    void PostOrderTraversal(Node *T)
    {
        if (T != NULL)
        {
            PostOrderTraversal(T->left);
            PostOrderTraversal(T->right);
            cout << T->data << " ";
        }
    }
    Node *findNode(int x)
    {
        Node *temp = root;
        while (temp != NULL)
        {
            if (x == temp->data)
            {
                return temp;
            }
            else if (x < temp->data)
            {
                temp = temp->left;
            }
            else
            {
                temp = temp->right;
            }
        }
        return NULL;
    }
    bool deleteNode(int x)
    {
        Node *temp = findNode(x);
        if (temp == NULL)
        {
            return false;
        }
        else
        {
            if (temp->left == NULL && temp->right == NULL)
            {
                if (temp->parent->left == temp)
                {
                    temp->parent->left = NULL;
                }
                else
                {
                    temp->parent->right = NULL;
                }
                delete temp;
            }
            else if (temp->left == NULL || temp->right == NULL)
            {
                if (temp->left == NULL)
                {
                    if (temp->parent->left == temp)
                    {
                        temp->parent->left = temp->right;
                    }
                    else
                    {
                        temp->parent->right = temp->right;
                    }
                    temp->right->parent = temp->parent;
                    delete temp;
                }
                else
                {
                    if (temp->parent->left == temp)
                    {
                        temp->parent->left = temp->left;
                    }
                    else
                    {
                        temp->parent->right = temp->left;
                    }
                    temp->left->parent = temp->parent;
                    delete temp;
                }
            }
            else
            {
                Node *successor = temp->right;
                while (successor->left != NULL)
                {
                    successor = successor->left;
                }
                temp->data = successor->data;
                if (successor->parent->left == successor)
                {
                    successor->parent->left = successor->right;
                }
                else
                {
                    successor->parent->right = successor->right;
                }
                if (successor->right != NULL)
                {
                    successor->right->parent = successor->parent;
                }
                delete successor;
            }
            return true;
        }
    }
    int NumberOfNodes(Node *T)
    {
        if (T == NULL)
            return 0;
        else
            return 1 + NumberOfNodes(T->left) + NumberOfNodes(T->right);
    }
    bool leafNodes(Node *T)
    {
        int count = 0;
        while (T != NULL)
        {
            if (T->left == NULL && T->right == NULL)
            {
                count++;
            }
            T = T->right;
        }
        if (count == 0)
        {
            return false;
        }
        else
        {
            return true;
        }
    }

    int height(Node *T)
    {
        if (T == NULL)
        {
            return 0;
        }
        else
        {
            int height_left = height(T->left);
            int height_right = height(T->right);
            if (height_left > height_right)
            {
                return height_left + 1;
            }
            else
            {
                return height_right + 1;
            }
        }
    }
};

int main()
{
}