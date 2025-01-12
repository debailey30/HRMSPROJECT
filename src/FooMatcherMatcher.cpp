#include <iostream>

// Define the matcher class template
template <typename T>
class FooMatcherMatcher {
public:
    using is_gtest_matcher = void;

    // MatchAndExplain method
    bool MatchAndExplain(const T& value, std::ostream* os) const {
        // Implement your matching logic here
        // For example, let's say we are checking if value is greater than 10
        if (value > 10) {
            return true;
        } else {
            if (os) {
                *os << "value " << value << " is not greater than 10";
            }
            return false;
        }
    }

    // DescribeTo method
    void DescribeTo(std::ostream* os) const {
        *os << "is greater than 10";
    }

    // DescribeNegationTo method
    void DescribeNegationTo(std::ostream* os) const {
        *os << "is not greater than 10";
    }
};

// Optional: Main function to test the matcher
int main() {
    FooMatcherMatcher<int> matcher;
    int testValue = 5;
    std::ostringstream os;
    bool result = matcher.MatchAndExplain(testValue, &os);

    std::cout << "Match result: " << (result ? "true" : "false") << std::endl;
    std::cout << "Explanation: " << os.str() << std::endl;

    return 0;
}