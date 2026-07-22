class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        vector<int>ans(gain.size()+2,0);
            for(int i=0;i<gain.size();i++){
                ans[i+1]=ans[i]+gain[i];
            }
            int maxi=INT_MIN;
        for(int i=0;i<ans.size();i++){
            maxi=max(maxi,ans[i]);
        }
        return maxi;
    }
};