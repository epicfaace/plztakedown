// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

/**
 * @title Storage
 * @dev Store & retrieve value in a variable
 * @custom:dev-run-script ./scripts/deploy_with_ethers.ts
 */
contract Storage {

    // bytes32 data;

    // /**
    //  * @dev Store value in variable
    //  * @param d value to store
    //  */
    // function store(bytes32 d) public {
    //     data = d;
    // }

    /**
     * @dev Return value 
     * @return value of 'data'
     */
    function retrieve() public view returns (string memory){
        return "<style> h1 { text-transform: uppercase; } </style> <h1>plztakedown</h1> <h2>This website cannot be censored or taken down</h2> <a href='#'>Read more</a><br><br> <iframe width='560' height='315' src='https://www.youtube.com/embed/dQw4w9WgXcQ?autoplay=1&mute=1' allow='autoplay' frameborder='0' allowfullscreen></iframe>";
    }
}