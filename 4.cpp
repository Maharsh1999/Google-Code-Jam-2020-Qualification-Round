#include<bits/stdc++.h>
#define fast_io ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
#define forit(it, a) for(__typeof(a.begin()) it = a.begin(); it != a.end(); it++)
#define rep(i,f,t) for(i=f;i<(int)t;++i)
#define pb push_back
#define mp make_pair
#define all(a) begin(a),end(a)
#define F first
#define S second

const int inf = 1e9 + 5, N = 2e5 + 5, D1[] = { 0,0,1,-1 }, D2[] = { 1,-1,0,0 };

using namespace std;

void Constant(string& STRING){
    for(char& ch:STRING){
        if(ch=='1')
        {
            ch='0';
        }
        else if(ch=='0')
        {
            ch='1';
        }
    }
}

int main() 
{
    int T,B;
    cin >> T >> B;
    while(T--)
    {
        int i, j, r=-1, c=-1;
        char L, OK;
        string s(B,'?');
        for(i=1, j=0; j<B/2 ; i+=2)
        {
            if( i>10 && i%10==1)
            {
                if(c!=-1)
                {
                    cout << c+1 << endl;
                    cin >> L;
                    if(s[c]!=L) 
                    {
                        Constant(s);
                    }
                }
                else 
                {
                    cout << "1\n";
                    cin>>L;
                }
                if(r!=-1){
                    cout << r+1 << endl;
                    cin >> L;
                    if(s[r]!=L)
                    {
                        reverse(all(s));
                    }
                }
                else 
                {
                    cout << "1\n";
                    cin>>L;
                }
            }
            else
            {
                cout << j+1 << endl;
                cin >> s[j];
                cout << B-j << endl;
                cin >> s[B-1-j];
                if(s[j]==s[B-1-j])
                {
                    c=j;
                }
                else if(s[j]!=s[B-1-j])
                {
                    r=j;
                }
                ++j;
            }
        }
        cout << s << endl;
        cout.flush();
        cin>>OK;
        if(OK=='N')
        {
            exit(0);
            return 0;
        }
    }
}