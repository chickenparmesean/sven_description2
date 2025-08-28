# SLIDE 1

### **Gabriel Jaldon**  

- No. 16 on Sherlock ELO-based leaderboard
- Won 1/1 Cosmos-SDK Golang Contests
- Won 4/4 Rust Contests
- Won 2/2 Solana Contests
- Won 4/4 Rust Contracts Contests
- Won 5/5 Sherlock Contests with staked points
- Won 4/4 Sherlock Contests led


#### **Key Audits & Skills:**  

- **Zetachain** (Crosschain & Cosmos SDK): CometBFT-based consensus and EVM-equivalent execution.  
- **Seda Protocol**: Rust/WasmVM components with manual memory management.  
- **IOTA Rebased (Rust)**: Parallel transaction execution.  
- **Geth Forks & Optimism L2**: EVM-equivalent system with consensus-execution integration.  
- **CosmosEVM**: Integrated EVM with Cosmos-SDK.  
- **Rust Contracts** (WoofiSwap, GMX Solana): Security expertise in Rust FFI and memory safety.  

#### **C/C++ & Concurrency Expertise:**  
- Developed a C++ service for 2D/3D data processing, tackling low-level memory management.  
- Identified a double-free vulnerability in a multi-threaded C system, detecting subtle concurrency flaws.  


#### ** Good Fit** (put this left underneath)
Expertise in consensus flaws, parallel EVM execution, and Rust/C++ FFI security ensures robust auditing of complex architectures.

# SLIDE 2



#### **Auditing Methodology:**  
- Maps system properties to guide code review using documentation.  
- Compares to prior audits to anticipate vulnerabilities.  
- Uses code bookmarks, digital notes, and hand-drawn diagrams to track attack paths.  
- Leverages AI for attack theorizing and PoC development.  


#### **Notable Findings:**  
1. **Seda Protocol (Consensus Non-Determinism)**: Wildcard expressions in consensus filters caused divergent state roots, halting the chain.  
2. **Seda Protocol (VM Sandbox Escape)**: Panic in `call_result_write` import crashed validators via host-sandbox flaws.  
3. **Zetachain (Memory Management Bug)**: Rust FFI flaw allowed exploitation of memory management gaps, risking node crashes.  
####  **Best-Fit Scopes**: Consensus, MonadDB (TrieDB), Compiler & VM (MonadVM)  
**Relevant Experience**:  
- **Seda Protocol**: Found non-determinism in consensus filters causing chain halts and validator crashes via VM sandbox escapes.  
- **Zetachain**: Exploited Rust FFI memory management flaws to crash nodes.  
- **IOTA Rebased**: Detected race conditions in concurrent subsystems during parallel execution.  
**Why He’s a Good Fit**:  
His expertise in consensus flaws, parallel execution, and Rust/C++ FFI security ensures robust auditing of consensus, database, and VM components.



---