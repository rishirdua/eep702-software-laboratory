#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include<string.h>
char s1[100] = "rishirishirishirishirishir";
char s2[10] = "rishi";

int n1,n2;
int size = 0;
int m = 0; //number of threads
int sum = 0;

void StringPrint(long *s);
void *PrintHello(void *threadid)
{
	long tid;
	tid = (long)threadid;
	int start=0, end=0;
	int b=0,k=0;
	if(tid == 0) {
		start = 0;
	}
	else {
		start = tid*size - n2/2;
	}
	if(tid == m-1) {
		end = (m)*size - 1 + n1%m;
	}
	else{
		end = (tid+1)*size - 1 + n2/2;
	}
	printf("\nThread no: %ld\n", tid,start,end);
	int pos=0;	

	while(start <= end)
	{
		if(s1[start] == s2[b])
		{
			if(b == n2-1) {
				k++; b=-1; StringPrint(&tid);
			}
			start++;b++;
		}
		else if(b!=0) {
			b = 0;
		}
		else
		{	b = 0; start++;	}
	}
	sum = sum + k;
	printf("Total embeddings of s2 in s1 = %d\n",sum);
	pthread_exit(NULL);
}

void StringPrint(long *s)
{
	printf("match at thread: %ld\n",*s);
}

int main(int argc, char *argv[])
{

	pthread_t threads[m];
	int rc;
	long t;

	printf("Enter s1: ");
	scanf("%s", s1);
	printf("Enter s2: ");
	scanf("%s", s2);


	n1 = strlen(s1);n2 = strlen(s2);
	printf("Enter no of threads: "); 
	scanf("%d", &m);
	size = n1/m;
	for(t=0;t<m;t++){
		printf("\nCreating thread %ld\n", t);
		rc = pthread_create(&threads[t], NULL, PrintHello, (void *)t);	// Error Handling
		if (rc){
			printf("ERROR; return code from pthread_create() is %d\n", rc);
			exit(-1);
		}
	}


   /* Last thing that main() should do */
   pthread_exit(NULL);

}
