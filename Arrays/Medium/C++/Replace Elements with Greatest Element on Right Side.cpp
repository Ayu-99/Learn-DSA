class Solution {
public:
    vector<int> replaceElements(vector<int>& a) {
        int n = a.size();
        vector<int> ans;
        int max = a[n-1];
        ans.push_back(-1);
        for(int i=n-2;i>=0;i--){
            ans.push_back(max);
            if(a[i]>=max){
                 max = a[i];
            }         
        }
        reverse(ans.begin(),ans.end());
        return ans;
    }
};
