#include <iostream.h>
#include <process.h>
#include <conio.h>
class node
{
   int info;
   node *left, *right;

public:
   node *create();
   void insert(int);
   void preorder(node *);
   void inorder(node *);
   void postorder(node *);
   void search(int);
   int count_leaf(node *);
   int count_total(node *);
} *root;
node *node::create()
{
   node *z;
   z = new node;
   return (z);
}
void node::search(int srch)
{
   int t = 0;
   node *p;
   p = root;

   while (p != NULL)
   {
      if (srch == p->info)
      {
         t = 1;
         break;
      }
      else if (srch < p->info)
      {
         p = p->left;
      }
      else if (srch > p->info)
      {
         p = p->right;
      }
   }

   if (t == 1)
      cout << "\nNode is Found ";
   else
      cout << "\nNode is NOT found ";
}
int node::count_total(node *p)
{
   if (p == NULL)
   {
      return (0);
   }
   else if (p->left == NULL && p->right == NULL)
   {
      return (1);
   }
   else
   {
      return (count_total(p->left) + count_total(p->right) + 1);
   }
}
int node::count_leaf(node *p)
{
   if (p == NULL)
   {
      return (0);
   }
   else if (p->left == NULL && p->right == NULL)
   {
      cout << "\t" << p->info;
      return (1);
   }
   else
   {
      return (count_leaf(p->left) + count_leaf(p->right));
   }
}
void node::insert(int x)
{
   node *n, *temp;
   n = create();
   n->left = NULL;
   n->info = x;
   n->right = NULL;
   if (root == NULL)
   {
      root = n;
      cout << "\nNode inserted...";
   }
   else
   {
      temp = root;
      while (temp != NULL)
      {
         if (n->info < temp->info)
         {
            if (temp->left == NULL)
            {
               temp->left = n;
               cout << "\n Node is inserted..";
               break;
            }
            else
            {
               temp = temp->left;
            }
         }
         else if (n->info > temp->info)
         {
            if (temp->right == NULL)
            {
               temp->right = n;
               cout << "\n Node is inserted..";
               break;
            }
            else
            {
               temp = temp->right;
            }
         }
         else
         {
            cout << "\nNode should not repeated...";
            break;
         }
      }
   }
}
void node::preorder(node *p)
{
   if (p != NULL)
   {
      cout << "\t" << p->info;
      preorder(p->left);
      preorder(p->right);
   }
}

void node::postorder(node *p)
{
   if (p != NULL)
   {
      postorder(p->left);
      postorder(p->right);
      cout << "\t" << p->info;
   }
}

void node::inorder(node *p)
{
   if (p != NULL)
   {
      inorder(p->left);
      cout << "\t" << p->info;
      inorder(p->right);
   }
}

void main()
{
   clrscr();
   node obj;
   int ch, n, z;
   do
   {
      cout << "\nEnter your choice= ";
      cout << "\n1:Insert\n2:Preorder\n3:Inorder\n4:Postorder\n5:Count Leaf\n6:Count Total\n7:Search\n8:Exit..";
      cin >> ch;
      switch (ch)
      {
      case 1:
         cout << "\n Enter val to insert=";
         cin >> n;
         obj.insert(n); // call
         break;
      case 2:
         obj.preorder(root); // call
         break;
      case 3:
         obj.inorder(root);
         break;
      case 4:
         obj.postorder(root);
         break;
      case 5:
         z = obj.count_leaf(root);
         cout << "\nTotal Leaf nodes=" << z;
         break;
      case 6:
         z = obj.count_total(root);
         cout << "\nTOtal nodes=" << z;
         break;
      case 7:
         cout << "\nEnter val to search= ";
         cin >> n;
         obj.search(n); // call
         break;
      case 8:
         exit(1);
      }
   } while (ch != 8);
   getch();
}
