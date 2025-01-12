// Integration test file 
// filepath: /C:/Users/DeeAnn/Desktop/HRMSPROJECT/build/Release/test_integrstions.cpp
#include <gtest/gtest.h>

// Sample test case
TEST(SampleTest, Test1) {
    EXPECT_EQ(1, 1);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}