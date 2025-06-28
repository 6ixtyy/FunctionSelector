# FunctionSelector
🌐 **[Live Demo](https://6ixtyy.github.io/FunctionSelector/)**

A web-based tool for calculating Ethereum function selectors and detecting selector collisions. This tool is essential for smart contract developers and security researchers working with Ethereum smart contracts.

## What is FunctionSelector?

FunctionSelector is a simple, lightweight web application that helps developers:
- Calculate the 4-byte function selector for any Ethereum function signature
- Check for potential selector collisions between different function signatures
- Understand the importance of selector uniqueness in smart contract security

## Features

- **Function Selector Calculator**: Convert any function signature to its corresponding 4-byte selector
- **Collision Detection**: Check if two different function signatures produce the same selector
- **Copy to Clipboard**: Easy one-click copying of calculated selectors
- **Modern UI**: Clean, responsive interface built with Tailwind CSS
- **No Dependencies**: Runs entirely in the browser using CDN resources

## Usage

1. **Open the application**: Simply open `Index.html` in any modern web browser
2. **Calculate a selector**:
   - Enter a function signature (e.g., `transfer(address,uint256)`)
   - Click "Calculate Selector"
   - Copy the resulting 4-byte selector
3. **Check for collisions**:
   - Enter two different function signatures
   - Click "Check Collision"
   - View whether they produce the same selector

## How it Works

Function selectors are the first 4 bytes of the Keccak-256 hash of the function signature. For example:
- Function signature: `transfer(address,uint256)`
- Keccak-256 hash: `0xa9059cbb2ab09eb219583f4a59a5d0623ade346d962bcd4e46b11da047c9049b`
- Function selector: `0xa9059cbb`

## Security Importance

Function selector collisions can lead to critical vulnerabilities in:
- **Proxy patterns**: Where the same selector might call different functions
- **Fallback functions**: Unexpected function calls due to selector conflicts
- **Contract upgrades**: Potential security issues during contract upgrades

This tool helps developers identify and avoid such collisions during the development phase.


## Example Usage

```javascript
// Function signature examples:
"transfer(address,uint256)" → 0xa9059cbb
"approve(address,uint256)" → 0x095ea7b3
"balanceOf(address)" → 0x70a08231
```


**Built with ❤️ by [Zaki](https://github.com/6ixtyy)**

*For smart contract security and development best practices.*
