pragma solidity ^0.5.0;

contract PeerToPeerLending {
    struct Loan {
        uint loanId;
        address payable borrower;
        address payable lender;
        uint loanAmount;
        uint interestRate;
        uint repaymentTerm;
        uint fundAmount;
        uint amountPayed;
        bool funded;
        bool repaid;
        uint balanceRemaning;
        uint amountOwed;
    }

    address payable company;
    address payable owner;
    uint balanceRemaning;
    uint companyRate =1;

    constructor() public {
        company = owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, 'You are not the owner');
        _;
    }

    function deposit() public payable {}

    Loan[] public loans;
    uint public loanIdCounter;

    event LoanCreated(uint loanId, address borrower, uint loanAmount);
    event LoanFunded(uint loanId, address lender, uint fundAmount);
    event LoanPayment(uint loanId, uint repaymentAmount);
    event LoanFullyRepaid(uint loanId);

    function createLoan(uint _loanAmount, uint _interestRate, uint _repaymentTerm) external {
        require(_loanAmount > 0, "Loan amount must be greater than 0");
        require(_interestRate > 0, "Interest rate must be greater than 0");
        require(_repaymentTerm > 0, "Repayment term must be greater than 0");

        uint loanId = loanIdCounter++;
        Loan memory newLoan = Loan(
            loanId,
            msg.sender,
            address(0),
            _loanAmount,
            _interestRate,
            _repaymentTerm,
            0,
            0,
            false,
            false,
            0,
            0
        );
        loans.push(newLoan);

        emit LoanCreated(loanId, msg.sender, _loanAmount);
    }

    // Fund a Loan
    function fundLoan(uint _loanId) external payable {
        Loan storage loan = loans[_loanId];
        require(!loan.funded, "Loan has already been funded");
        require(msg.value >= loan.loanAmount, "Insufficient funds to cover loan");

        loan.borrower.transfer(loan.loanAmount); // Transfer the loan amount from lender to borrower
        loan.lender = msg.sender; // Set the lender address
        loan.funded = true;
        loan.fundAmount = loan.loanAmount;
        loan.balanceRemaning = loan.loanAmount;
        loan.amountOwed = loan.loanAmount;
        uint amount = msg.value;
        companyRate = (amount * 1) / 100;
        loan.amountOwed = msg.value * (loan.interestRate * 1) / 100;
        loan.amountOwed += companyRate;



        

        emit LoanFunded(_loanId, msg.sender, loan.loanAmount);
    }

    function repayLoan(uint _loanId) external payable{
        Loan storage loan = loans[_loanId];
        require(loan.funded, "Loan has not been funded");
        require(!loan.repaid, "Loan has already been repaid");
        require(msg.value > 0, "Repayment amount must be greater than 0");

        uint amount = msg.value;
        uint onePercent = (amount * 1) / 100;
        uint remaining = amount - onePercent;
        company.transfer(onePercent);
        loan.lender.transfer(remaining);
        loan.balanceRemaning -= amount;
        loan.amountPayed += amount;

        if (loan.balanceRemaning == 0) {
            loan.repaid = true;
            emit LoanFullyRepaid(_loanId);
        }

        emit LoanPayment(_loanId, msg.value);
    }

    function getLoanDetails(uint _loanId) external view returns (uint, address, address, uint, uint, uint, uint, uint, bool, bool) {
        require(_loanId < loans.length, "Invalid loan ID");

        Loan memory loan = loans[_loanId];
        return (
            loan.loanId,
            loan.borrower,
            loan.lender,
            loan.loanAmount,
            loan.interestRate,
            loan.repaymentTerm,
            loan.fundAmount,
            loan.amountPayed,
            loan.funded,
            loan.repaid
        );
    }

    function() external payable {}
}