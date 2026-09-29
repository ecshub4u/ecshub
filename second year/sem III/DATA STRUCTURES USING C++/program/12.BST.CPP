#include<iostream.h>
#include<process.h>
#include<conio.h>
class	node
{
	int     info;
	node   *left,*right;
	public:
	node* create();
	void  insert(int);
	void  preorder(node*);
	void  inorder(node*);
	void  postorder(node*);
}*root;
node*  node::create()
{
    node  *z;
    z=new node;
    return(z);
}
void   node::insert(int   x)
{
   node   *n,*temp;
   n=create();
   n->left=NULL;
   n->info=x;
   n->right=NULL;
   if(root==NULL)
   {
     root=n;
     cout<<"\nNode inserted...";
   }
   else
   {
       temp=root;
       while(temp!=NULL)
       {
	   if(n->info<temp->info)
	   {
	      if(temp->left==NULL)
	      {
		temp->left=n;
		cout<<"\n Node is inserted..";
		break;
	      }
	      else
	      {
		temp=temp->left;
	      }
	   }
	   else if(n->info>temp->info)
	   {
	      if(temp->right==NULL)
	      {
		temp->right=n;
		cout<<"\n Node is inserted..";
		break;
	      }
	      else
	      {
		temp=temp->right;
	      }
	   }
	   else
	   {
	       cout<<"\nNode should not repeated...";
	       break;
	   }
       }

   }
   }
   void   node::preorder(node   *p)
   {
     if(p!=NULL)
     {
       cout<<"\t"<<p->info;
       preorder(p->left);
       preorder(p->right);
     }
   }

   void   node::postorder(node   *p)
   {
     if(p!=NULL)
     {
       postorder(p->left);
       postorder(p->right);
       cout<<"\t"<<p->info;
     }
   }

   void  node::inorder(node   *p)
   {
       if(p!=NULL)
       {
	  inorder(p->left);
	  cout<<"\t"<<p->info;
	  inorder(p->right);
       }
   }

   void main()
   {
       clrscr();
       node   obj;
       int ch,n;
       do
       {
	  cout<<"\nEnter your choice= ";
	  cout<<"\n1:Insert\n2:Preorder\n3:Inorder\n4:Postorder\n5:Exit..";
	  cin>>ch;
	  switch(ch)
	  {
	     case 1:
		   cout<<"\n Enter val to insert=";
		   cin>>n;
		   obj.insert(n);  //call
		   break;
	     case 2:
		  obj.preorder(root);  //call
		  break;
	     case 3:
		    obj.inorder(root);
		  break;
	     case 4:
			obj.postorder(root);
			break;
	     case    5:
		   exit(1);
	  }
	  }while(ch!=5);
	  getch();
   }

















