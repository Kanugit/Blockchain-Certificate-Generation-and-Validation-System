// SPDX-License-Identifier: MIT 
pragma solidity ^0.5.16;

contract Migrations {
    address public owner;
    uint public last_completed_migration;

    modifier restricted() {
        // Require that the sender is the owner
        require(msg.sender == owner, "You are not the owner");
        _;
    }

    // Constructor with public visibility
    constructor() public {
        owner = msg.sender;
    }

    function setCompleted(uint completed) public restricted {
        last_completed_migration = completed;
    }

    function upgrade(address new_address) public restricted {
        Migrations upgraded = Migrations(new_address);
        upgraded.setCompleted(last_completed_migration);
    }
}
