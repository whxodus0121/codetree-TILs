#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int n;
int t[15];
int p[15];
int dp[16];

int main() {
    // 여기에 코드를 작성해주세요.
    cin>>n;

    for(int i=0;i<n;i++){

        cin>>t[i]>>p[i];
    }

    for(int i=n-1;i>=0;i--){
        
        if(t[i]+i<=n){

            dp[i]=max(dp[i+t[i]]+p[i],dp[i+1]);
        }
        else dp[i]=dp[i+1];
    }

    cout<<dp[0];
    return 0;
}