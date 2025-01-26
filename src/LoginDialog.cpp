#include <QDialog>
#include <QMessageBox>
#include "UserRoles.h"
#include "LoginDialog.h"
#include "ui_LoginDialog.h" // Include the generated header file
#include <QtCore/QVariant>

/// @brief Login dialog class for user authentication

/**
 * @class LoginDialog
 * @brief A dialog for user login in the HRMS project.
 *
 * The LoginDialog class provides a user interface for logging into the system.
 * It includes fields for entering a username and password, and buttons for
 * submitting the login information or recovering a forgotten username.
 *
 * @inherits QDialog
 */

LoginDialog::LoginDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::LoginDialog)
{
    ui->setupUi(this); // Set up the user interface from the Designer file
}

LoginDialog::~LoginDialog() {
    delete ui;
}

UserRole LoginDialog::getUserRole() const {
    return userRole;
}

/**
 * @brief Slot function called when the login button is clicked.
 *
 * This function is triggered when the user clicks the login button. It validates
 * the username and password, and logs the user in if the credentials are correct.
 */
void LoginDialog::on_loginButton_clicked() {
    // TODO: Implement the login functionality
    // Validate the username and password, and log the user in if the credentials are correct
}

void LoginDialog::on_forgotUsernameButton_clicked() {
    // TODO: Implement the username recovery process
    // Display a message box to inform the user about the username recovery process
}