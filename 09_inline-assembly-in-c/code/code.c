#include <stdio.h>
#include <sys/time.h>
#include <math.h>

/* Declaration of functions */
int gcd_orig( int a, int b ); //Calculates GCD using C code
int gcd_opt( int a, int b ); //Calculates GCD using Assembly code
int msb_orig(unsigned int inp); //Finds MSB using C code
int msb_opt(unsigned int inp); //Finds MSB using Assembly code
float cosx_orig(float indegree); //Calculates cos of angle in degree using C code
float cosx_opt(float indegree); //Calculates cos of angle in radian using Assembly code

int main() {
	//stores time for running the code
	struct timeval t1, t2;
	double elapsedTime;
	 
	
	/* GCD and LCM */

	
	int a, b, x, y, gcd, lcm;
	printf("\nGCD LCM calculator\n");
	printf("Enter two integers\n");
	scanf("%d%d", &x, &y);
	 
	a = x; b = y;
	int counter;
	//Original 
	//Call the code in a loop as the least count of time is low
	gettimeofday(&t1, NULL); 
	for (counter=0; counter<1000000; counter++) {
		gcd = gcd_orig(a, b);
	}
	gettimeofday(&t2, NULL);
	#ifdef GCD
	printf("Greatest common divisor of %d and %d = %d\n", x, y, gcd);
	#else
	lcm = (x*y)/gcd;
	printf("Least common multiple of %d and %d = %d\n", x, y, lcm);
	#endif
	elapsedTime = (t2.tv_sec - t1.tv_sec) * 1000.0;      // sec to ms
	elapsedTime += (t2.tv_usec - t1.tv_usec) / 1000.0;   // us to ms
	printf("Unoptimized time is %f ms\n", elapsedTime);
	
	//optimized code
	//Call the code in a loop as the least count of time is low
	gettimeofday(&t1, NULL); 
	for (counter=0; counter<1000000; counter++) {
		gcd = gcd_opt(a, b);
	}
	gettimeofday(&t2, NULL);
	//check compilation directive and take action accordingly
	#ifdef GCD
	printf("Greatest common divisor of %d and %d = %d\n", x, y, gcd);
	#else
	lcm = (x*y)/gcd;
	printf("Least common multiple of %d and %d = %d\n", x, y, lcm);
	#endif
	elapsedTime = (t2.tv_sec - t1.tv_sec) * 1000.0;      // sec to ms
	elapsedTime += (t2.tv_usec - t1.tv_usec) / 1000.0;   // us to ms
	printf("Optimized time is %f ms\n", elapsedTime);

	
	/* MSB */


	unsigned int v, inp, msb;
	printf("\nMSB of larger integer \n");
	printf("Enter two integers\n");
	scanf("%d%d", &x, &y);
	if (x>y)
		inp = x;
	else
		inp = y;
	v = inp;
	printf("The larger integer is %d\n", inp);
	
	//Unoptimized
	gettimeofday(&t1, NULL); 
	for (counter=0; counter<1000000; counter++) {
		msb = msb_orig(v);
	}
	gettimeofday(&t2, NULL);
	printf("MSB is %d\n", msb);
	elapsedTime = (t2.tv_sec - t1.tv_sec) * 1000.0;      // sec to ms
	elapsedTime += (t2.tv_usec - t1.tv_usec) / 1000.0;   // us to ms
	printf("Unoptimized time is %f ms\n", elapsedTime);

	//Optimized
	gettimeofday(&t1, NULL); 
	for (counter=0; counter<1000000; counter++) {
		msb = msb_orig(v);
	}
	gettimeofday(&t2, NULL);
	printf("MSB is %d\n", msb);
	elapsedTime = (t2.tv_sec - t1.tv_sec) * 1000.0;      // sec to ms
	elapsedTime += (t2.tv_usec - t1.tv_usec) / 1000.0;   // us to ms
	printf("Optimized time is %f ms\n", elapsedTime);


	/* COS of Angle */


	float uinp, inangle, cosx;
	printf("\ncos of angle in degrees \n");
	printf("Enter angle\n");
	scanf("%f", &uinp);
	inangle = uinp;
	
	//Original code
	gettimeofday(&t1, NULL); 
	for (counter=0; counter<1000000; counter++) {
		cosx = cosx_orig(inangle);
	}
	gettimeofday(&t2, NULL);
	printf("cos of of %f = %f\n", inangle, cosx);
	elapsedTime = (t2.tv_sec - t1.tv_sec) * 1000.0;      // sec to ms
	elapsedTime += (t2.tv_usec - t1.tv_usec) / 1000.0;   // us to ms
	printf("Unoptimized time is %f ms\n", elapsedTime);
	
	//optimized code
	gettimeofday(&t1, NULL); 
	for (counter=0; counter<1000000; counter++) {
		cosx = cosx_opt(inangle);
	}
	gettimeofday(&t2, NULL);
	printf("cos of of %f = %f\n", inangle, cosx);
	elapsedTime = (t2.tv_sec - t1.tv_sec) * 1000.0;      // sec to ms
	elapsedTime += (t2.tv_usec - t1.tv_usec) / 1000.0;   // us to ms
	printf("Optimized time is %f ms\n", elapsedTime);

	return 0;
}

//unoptimized helper function
int gcd_orig(int a, int b) {
	/* Compute Greatest Common Divisor using Euclid's Algorithm */
	int t;
	while (b != 0) {
	    t = b;
	    b = a % b;
	    a = t;
	}
	return a;
}

//optimized helper function
int gcd_opt( int a, int b ) {
    int result ;
    /* Compute Greatest Common Divisor using Euclid's Algorithm */
    __asm__ __volatile__ ( "movl %1, %%eax;"
                          "movl %2, %%ebx;"
                          "CONTD: cmpl $0, %%ebx;"
                          "je DONE;"
                          "xorl %%edx, %%edx;"
                          "idivl %%ebx;"
                          "movl %%ebx, %%eax;"
                          "movl %%edx, %%ebx;"
                          "jmp CONTD;"
                          "DONE: movl %%eax, %0;" : "=g" (result) : "g" (a), "g" (b)
    );
    return result ;
}


//unoptimized helper function
int msb_orig(unsigned int inp) {
	 return floor((log(inp)/log(2))) + 1;
}

//optimized helper function
int msb_opt(unsigned int v) {
	unsigned int r;
	while (v >>= 1) // unroll for more speed...
	{
	  r++;
	}
	return v;
}


//unoptimized helper function
float cosx_orig(float indegree) {
	float inrad = indegree*3.14/180;
	return (float)cos((double)inrad);	
	
}

//unoptimized helper function
float cosx_opt(float indegree) {
    float result, two_right_angles = 180.0f ;

    __asm__ __volatile__ ( "fld %1;"
                            "fld %2;"
                            "fldpi;"
                            "fmulp;"
                            "fdivp;"
                            "fcos;"
                            "fstp %0;" : "=m" (result) : 
				"g"(two_right_angles), "g" (indegree)
    ) ;
    return result ;
}

