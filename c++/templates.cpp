struct hashes
{
    string s;
    int base, mod;
    vector<long long> powers = {1}, psa = {0};

    hashes(string S, int b = 131, int m = 1000000007)
    {
        s = S;
        base = b;
        mod = m;
        for (int i = 0; i < s.size(); i++)
        {
            powers.push_back(powers.back() * base % mod);
            psa.push_back((psa.back() + s[i] * powers[i]) % mod);
        }
    }

    long long get(int l, int r)
    {
        return (psa[r + 1] - psa[l] + mod) * powers[s.size() - r] % mod;
    }
};