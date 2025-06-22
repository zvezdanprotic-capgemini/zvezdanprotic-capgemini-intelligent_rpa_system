TASKS = {
    "open_account": [
        {
            "step": "Verify identity",
            "description": "Confirm the user's identity with official documents.",
            "required_documents": [
                "Government-issued ID (e.g., passport, national ID card)",
                "Proof of address (e.g., utility bill, rental agreement)"
            ]
        },
        {
            "step": "Create account in core system",
            "description": "Create the bank account in the core banking system.",
            "required_documents": []
        }
    ],
    "apply_loan": [
        {
            "step": "Collect documents",
            "description": "Gather all necessary documents to support the loan application.",
            "required_documents": [
                "Proof of income (e.g., salary slips, tax returns)",
                "Recent bank statements (last 3–6 months)",
                "Government-issued ID",
                "Loan purpose document (e.g., invoice, proposal, estimate)"
            ]
        },
        {
            "step": "Evaluate eligibility",
            "description": "Analyzes the provided documents along with bank records to decide whether the loan should be approved.",
            "required_documents": [
                "All user-submitted documents",
                "Internal bank records (e.g., account history, credit score)"
            ]
        }
    ]
}