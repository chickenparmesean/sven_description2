### Gabriel Jaldon  

- **Contest Wins**:  
  - **4/4 Rust Contest Wins** (explicitly stated)  
  - **2/2 Solana Contest Wins** (explicitly stated)  
  - **2/2 Cosmos-SDK Golang Contest Wins** (explicitly stated)  
  - **6/6 Sherlock Contest Wins** with staked points (explicitly stated)  
  - **5/5 Sherlock Contests Led** (explicitly stated)  

- **Background**:  
  - **10+ years software dev**: Transitioned from **full-stack web development and DevOps** (troubleshooting production issues, optimizing databases/websites for large traffic) to **Web3 smart contract development and auditing** (Solidity/EVM, DeFi).  
  - **Languages**: Solidity, Rust, Go, JavaScript (Node.js, React), Python, Bash, Clojure, OCaml, Haskell, C/C++ (explicitly stated).  

- **Private Audit Highlights**:  
  - **IOTA Chain & L2**: Analyzed Rust/Go FFI for Sui fork compatibility and parallel execution risks (explicitly stated).  
  - **Optimism L2**: Validated EVM parity and sequencer logic under high-load scenarios (explicitly stated).  
  - **GMX & Rain Solana**: Discovered critical flaws in Rust-based DeFi contracts (explicitly stated).  
  - **Reserve Asset-backed Stablecoin**: Audited Solidity contracts for peg resilience and oracle manipulation (explicitly stated).  
  - **Vaultcraft Yield Aggregator**: Audited Solidity contracts for reentrancy and reward distribution gaps (explicitly stated).  

- **Key Audits & Skills**:  
  - **OpenZeppelin AA Stack**: Audited Bundler and Paymaster contracts for griefing and DoS risks (explicitly stated).  
  - **Cosmos SDK Chains**: Validator slashing logic and cross-chain IBC integrations (explicitly stated).  
  - **DeFi Protocols**: GMX, Rain, Uniswap v3 (Solidity/Rust) (explicitly stated).  

- **Good Fit**:  
  Gabriel’s **direct experience with Geth forks** (e.g., Optimism L2, IOTA Smart Contracts) and **EVM-compatible AA frameworks** (e.g., OpenZeppelin) aligns with Incentiv’s scope. His hybrid stack expertise (Go/Rust/Solidity) ensures rigorous validation of Geth-based protocol modifications and secure implementation of AA smart contracts.  

## SLIDE 2  

- **Auditing Methodology**:  
  - **Initial Phase**: Merges **Geth protocol diffs** with **AA contract specs** to map attack surfaces (e.g., Bundler ↔ EVM integration).  
  - **Critical Path Prioritization**: Focuses on **FFI risks in Geth modifications** (e.g., memory management), **AA contract invariants**, and **gas model edge cases**.  
  - **Note-Taking**:  
    - **Code Bookmarks**: Flags **unbounded memory in Geth sequencer logic** (from IOTA audit) and **reentrancy-prone AA hooks** (from Vaultcraft audit).  
    - **Digital Notes**: Structured via **attack trees** for transaction bundling and wallet recovery flows.  
    - **Paper Mind Maps**: Visualizes **validator ↔ execution layer interactions** and **token fee conversion mechanics**.  
  - **AI & Tools**: Leverages AI for rapid POC drafting and static analysis of **Go (Geth)** and **Rust (FFI)** codebases (~5,000 lines).  

- **Notable Findings**:  
  1. **IOTA Rebased (FFI Memory Leak)**: Golang FFI code failed to garbage collect parallel execution threads, risking node crashes (explicitly stated).  
  2. **Optimism L2 (EVM Parity Drift)**: Sequencer logic mishandled L2 gas costs during L1 reorgs, creating fee calculation arbitrage (explicitly stated).  
  3. **GMX Solana (Rust Reentrancy)**: Callbacks in margin contracts allowed recursive liquidations, draining liquidity pools (explicitly stated).  
  4. **Vaultcraft (Reward Sybil)**: Exploited vesting logic to multiply yield claims in a Solidity-based aggregator (explicitly stated).  

- **Relevant Experience**:  
  - Specializes in **Geth-based L2s** (e.g., Optimism, IOTA) and **hybrid stack audits** (Go/Rust/Solidity).  
  - Expert in **DeFi-specific vulnerabilities** (reentrancy, reward manipulation) and **AA frameworks** (EIP-4337, Bundler logic).  

### Sammy  

- **Contest Wins**:  
  - **Top 3 in Story Protocol Geth Fork Contest**  
  - **Top 5 in Biconomy Account Abstraction Contest**  

- **Background**:  
  - **Blockchain Infrastructure Expertise**: Focus on **ZK/optimistic rollups, Cosmos SDK chains, and smart contract VMs**.  
  - **DeFi Specialization**: Deep knowledge of **lending protocols, voting escrow systems, AMMs, NFTs, staking, yield farming, and cross-chain DeFi**.  
  - **Languages**: Solidity, Rust, Go.  

- **Private Audit Highlights**:  
  - **LayerZero (Solidity, EVM)**: Analyzed cross-chain messaging security and state consistency edge cases.  
  - **CosmWasm VM (Rust, Go, Cosmos SDK)**: Validated execution layer integrity and sandboxing mechanisms.  
  - **Brevis ZK Prover (Rust, Go)**: Audited ZK proof generation/verification logic for soundness and DoS risks.  
  - **Irys VM (Rust) {ONGOING}**: Assessing runtime security and gas metering for decentralized storage systems.  

- **Key Audits & Skills**:  
  - **ZK Cryptography**: Audited **Aleo** and **Gamma Brevis Rewarder** for cryptographic vulnerabilities.  
  - **Geth Forks**: Experience with **Story Protocol** to identify risks in protocol-level modifications.  
  - **Account Abstraction**: Applied **Biconomy** audit insights to secure smart contract wallets and transaction bundling workflows.  
  - **VM Security**: Specializes in **CosmWasm, EVM, and custom VMs** for runtime safety and gas model precision.  

- **Good Fit**:  
  Sammy’s **direct experience with Geth forks** (e.g., Story Protocol) and **Account Abstraction frameworks** (e.g., Biconomy) aligns with Incentiv’s native AA implementation (ERC-4337) and EVM compatibility goals. His **ZK cryptography expertise** (Aleo, Gamma Brevis) and **cross-chain bridge analysis** ensures rigorous validation of Incentiv’s **integrated DEX gas swapping** and **auto-generated liquidity pools**. His **VM security background** (CosmWasm, Irys) directly supports auditing protocol-level components like **TransferGate** and **Token/NFT Factory** for execution layer robustness.  

- **Auditing Methodology**:  
  - **Initial Phase**: Cross-references **Geth protocol diffs** with **AA contract specs** to identify gas model inconsistencies or FFI risks.  
  - **Critical Path Focus**: Prioritizes **wallet recovery flows**, **transaction bundling invariance**, and **validator ↔ execution layer interactions** under DAO PoA.  
  - **Tooling**: Leverages AI for static analysis of **Solidity AA contracts** and **Go-based Geth modifications** (~10k lines).  
  - **Documentation**: Flags **unbounded loops in auto-swapping logic** (from LayerZero audit) and **ZK proof recursion gaps** (from Brevis audit) via attack trees.  

- **Relevant Experience**:  
  - Expert in **hybrid ZK/EVM architectures** (Story Protocol) and **cross-chain state validation** (LayerZero).  
  - Proven track record in **DeFi-specific risks** (reentrancy, incentive manipulation) and **validator governance models** (DAO PoA).  
  - Ongoing work on **Irys VM {ONGOING}** provides real-time insights into runtime security for decentralized applications.

### bin2chen  

- **Contest Wins**:  
  - **Top 5 in Biconomy Account Abstraction Contest** (2 findings)  
  - **ZKSync Era Contests** (3 findings across 2 contests)  
  - **Story Protocol Geth Fork Contest** (top 3 finish)  
  - **Optimism Fault Proofs Audit** (1 finding in Jun '25)  

- **Background**:  
  - **DeFi & Account Abstraction Expert**: Focused on **lending protocols, AMMs, NFTs, cross-chain DeFi, and derivative mechanisms**.  
  - **Technical Stack**: Solidity, Rust, Go, with emphasis on **EVM-compatible systems**, **Rust/Go VMs**, and **AA frameworks**.  
  - **Protocol-Level Auditing**: Experience with **ZK infrastructure** (Opus), **Geth forks** (ZKSync Era, Optimism), and **validator governance models**.  

- **Private Audit Highlights**:  
  - **Biconomy Smart Contract Wallet**: Exposed signature validation flaws and counterfactual wallet control risks.  
  - **Optimism Fault Proofs**: Analyzed **Geth-based sequencer logic** for DOS attack risks during L1 reorgs.  
  - **ZKSync Era System Contracts**: Identified gas refund mismanagement and fallback logic gaps.  
  - **LayerZero Cross-Chain Bridge**: Validated state consistency and replay attack mitigations in EVM-compatible systems.  
  - **GMX Solana Audit**: Discovered reentrancy risks and liquidation logic flaws in Rust-based DeFi protocols.  

- **Key Audits & Skills**:  
  - **Account Abstraction**: Audited **Biconomy Smart Contract Wallet** for signature malleability and recovery vulnerabilities.  
  - **Geth Forks**: Analyzed **ZKSync Era** and **Optimism** for protocol diffs, execution layer edge cases, and sequencer logic.  
  - **DeFi Protocols**: GMX (3 audits), Dopex (8 findings), Panoptic (4 findings), Notional (8 findings), Y2K (11 findings), Astaria (10 findings), Redacted Cartel (4 findings).  
  - **Cross-Chain Security**: LayerZero, Hyperlane Sealevel, TapiocaOFT, and Stargate integrations.  
  - **VM & Runtime Security**: CosmWasm (Go/Rust), Cairo-based Opus, and EVM parity validation.  

- **Good Fit**:  
  bin2chen’s **direct experience with Biconomy’s AA framework** and **Optimism/ZKSync Era Geth forks** aligns with Incentiv’s native Account Abstraction (ERC-4337) and EVM compatibility requirements. His **DeFi-specific findings** (GMX, Dopex, Panoptic) directly address risks in Incentiv’s **incentive distribution** and **integrated DEX gas swapping**. His **cross-chain bridge analysis** (LayerZero, Hyperlane) ensures robust validation of Incentiv’s auto-swapping liquidity pools and validator ↔ execution layer interactions under DAO PoA.  

- **Auditing Methodology**:  
  - **Initial Phase**: Cross-references **Geth protocol diffs** with **AA contract specs** to map gas model inconsistencies or FFI risks.  
  - **Critical Path Focus**: Prioritizes **wallet recovery flows**, **transaction bundler edge cases**, and **validator slashing logic** under DAO PoA.  
  - **Tooling**: Leverages AI for static analysis of **Solidity AA contracts** and **Go-based Geth forks** (~10k lines).  
  - **Documentation**: Flags **unbounded loops in cross-chain swaps** (from LayerZero audit) and **signature replay risks** (from Biconomy audit) via attack trees and runtime flow diagrams.  

- **Relevant Experience**:  
  - Specializes in **AA frameworks** (Biconomy, ZKSync) and **Geth forks** (Optimism, ZKSync Era) for protocol-level security.  
  - Expert in **DeFi-specific vulnerabilities** (reentrancy, oracle manipulation, liquidation gaps) and **cross-chain state validation** (Hyperlane, TapiocaOFT).  
  - Proven ability to audit **smart contract VMs** (CosmWasm, Cairo) and **validator infrastructure** (Stader Labs, LSD Network) for execution layer robustness.



### 0xadrii  

- **Contest Wins**:  
  - **Telcoin Wallet Audit** (2 high-severity findings, 5 medium)  
  - **Teller Finance Lending Vault** (2nd place, 8 high/5 medium findings)  
  - **TapiocaDAO Lending/Borrowing** (3 high/12 medium findings)  
  - **Cooler Protocol Peer-to-Peer Lending** (1 high-severity finding)  

- **Background**:  
  - **Account Abstraction & Modular Systems**: Specializes in **smart contract wallets** (Telcoin) and **upgradable proxy patterns** (Ubiquity Diamond Proxy).  
  - **Technical Focus**: Solidity, Rust, with emphasis on **ERC-4337 compliance**, **Diamond Proxy security**, and **cross-chain token mechanics**.  
  - **DeFi Logic Expertise**: Deep experience in **lending protocols**, **structured finance**, **staking rewards**, and **ERC-5725/20-based systems**.  

- **Private Audit Highlights**:  
  - **Telcoin Wallet**: Identified signature validation flaws and recovery path vulnerabilities in AA-enabled smart wallet architecture.  
  - **Ubiquity Diamond Proxy**: Validated access control logic and state variable consistency across facets in modular contracts.  
  - **TapiocaDAO**: Exposed over-collateralization gaps and cross-chain message replay risks in OFT integrations.  
  - **Aave v3.3**: Reviewed reward accrual, oracle integration, and token transfer edge cases in staking systems.  
  - **Midas & Asymmetry**: Secured vesting NFTs and staking emission logic for tokenized assets.  

- **Key Audits & Skills**:  
  - **Account Abstraction**: Direct experience with **Telcoin Wallet** and **ERC-4337 compliance** for smart contract wallets.  
  - **Modular Contracts**: Proven ability to audit **Diamond Proxy systems** (Ubiquity) and **facet-based upgrades**.  
  - **Lending/Borrowing Protocols**: Teller Finance (2nd place), TapiocaDAO (3 high findings), and Cooler Protocol (1 high finding).  
  - **Staking & Rewards**: Aave v3.3, Covalent Staking, and Yel Finance’s asset custody/swapping flows.  
  - **Cross-Chain DeFi**: TapiocaOFT, Renzo, and IPOR audits for state consistency and bridge logic.  

- **Good Fit**:  
  0xadrii’s **specialization in AA-enabled wallets** (Telcoin) and **modular contract security** (Ubiquity) aligns with Incentiv’s native Account Abstraction implementation (ERC-4337) and transaction bundling workflows. His **DeFi lending/borrowing expertise** (Teller, TapiocaDAO) ensures rigorous validation of Incentiv’s **integrated DEX gas swapping** and **liquidity pool generation**. His **cross-chain audit background** (TapiocaOFT, Renzo) directly supports securing auto-swapping mechanisms and validator ↔ execution layer interactions under DAO PoA.  

- **Auditing Methodology**:  
  - **Initial Phase**: Merges **ERC-4337 specs** with **Geth fork diffs** to map wallet recovery, paymaster, and bundler risks.  
  - **Critical Path Prioritization**: Focuses on **signature replay attacks**, **unbounded loops in staking flows**, and **validator governance bypasses**.  
  - **Note-Taking**: Flags **reentrancy-prone hooks** (from Teller audit) and **facet state conflicts** (Ubiquity) via attack trees.  
  - **AI & Tools**: Uses AI for static analysis of **Solidity AA contracts** and **Rust-based VMs** (~5k lines).  

- **Relevant Experience**:  
  - Expert in **smart contract wallets** (Telcoin) and **Geth-derived systems** for protocol-level security.  
  - Proven track record in **DeFi-specific vulnerabilities** (oracle manipulation, liquidation gaps) and **modular contract upgrades** (Ubiquity).  
  - Ongoing work on **TapiocaDAO** ensures real-time insights into cross-chain lending mechanics and OFT integrations.

---