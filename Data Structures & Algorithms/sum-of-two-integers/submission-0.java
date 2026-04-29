class Solution {
    public int getSum(int a, int b) {
        /* a -> sum, b -> carry
        python integers are arbitrarily large (not necessarily 32-bit), unlike java */
        while (b != 0) {
            int carry = (a & b) << 1;
            a = a ^ b;
            b = carry;
        }
        
        return a;
    }
}
