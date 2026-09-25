// Implementation of BST with node delete operation
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
	void  inorder(node*);
	void	del_leaf(node*,node*);
	void	del_one(node*,node*);
	void	del_two(node*);
	void	del(int);
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

   void  node::inorder(node   *p)
   {
       if(p!=NULL)
       {
	  inorder(p->left);
	  cout<<"\t"<<p->info;
	  inorder(p->right);
       }
   }

   void    node::del_leaf(node *parent,node *child)
   {
       if(child==parent->left)
       {
	   parent->left=NULL;
       }
       else if(child==parent->right)
       {
	  parent->right=NULL;
       }
       delete(child);
       cout<<"\nNode is Deleted...";
   }
   void   node::del_one(node *parent,node *child)
   {
      if(child==parent->left)
      {
	  if(child->left!=NULL)
	  {
	     parent->left=child->left;
	  }
	  else
	  {
	    parent->left=child->right;
	  }
      }
      else if(child==parent->right)
      {
	  if(child->right!=NULL)
	  {
	     parent->right=child->right;
	  }
	  else
	  {
	    parent->right=child->left;
	  }
      }
      delete(child);
      cout<<"\nNode is deleted..";
   }
   void  node::del_two(node *child)
   {
       node  *lft,*parent=NULL;
       lft=child->left;
       while(lft->right!=NULL)
       {
	   parent=lft;
	   lft=lft->right;
       }
       child->info=lft->info;
       if(parent==NULL)
       {
	  parent=child;
       }

       if(lft->left==NULL&&lft->right==NULL)
       {
	   del_leaf(parent,lft);
       }
       else
       {
	   del_one(parent,lft);
       }
   }

   void   node::del(int    srch)
   {
       int   f=0;
       node   *p,*c;
       p=c=root;
       while(c!=NULL)
       {
	    if(srch==c->info)
	    {
		f=1;
		break;
	    }
	    else if(srch<c->info)
	    {
	       p=c;
	       c=c->left;
	    }
	    else  if(srch>c->info)
	    {
	       p=c;
	       c=c->right;
	    }
       }

       if(f==1)
       {
	   if(c->left==NULL&&c->right==NULL)
	   {
	       del_leaf(p,c);
	   }
	   else  if(c->left!=NULL&&c->right!=NULL)
	   {
		del_two(c);
	   }
	   else
	   {
		del_one(p,c);
	   }
       }
       else
       {
	   cout<<"\nNode not Found ";
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
	  cout<<"\n1:Insert\n2:Inorder\n3:Delete\n4:Exit..";
	  cin>>ch;
	  switch(ch)
	  {
	     case 1:
		   cout<<"\n Enter val to insert=";
		   cin>>n;
		   obj.insert(n);  //call
		   break;
	     case 2:
		  obj.inorder(root);
		  break;
	     case 3:
		  cout<<"\nEnter node to delete= ";
		  cin>>n;
		  obj.del(n);
		  break;
	     case 4:
		   exit(1);
	  }
	  }while(ch!=4);
	  getch();
   }

















