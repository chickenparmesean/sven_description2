# Defsec Team  

## SLIDE 1  

- Top 50 on Code4rena All-time leaderboard  
- Found more than 90 High & Medium vulnerabilities in Audit Contests  
- Expert for Audits of L1 Blockchains and VM Implementations  

- **Key Audits & Skills:**  
  - **Cosmos EVM & Wasm**: Parallel execution across dual-VM architectures, focusing on cross-VM state consistency.  
  - **Core Chain (Bitcoin L1)**: Hybrid consensus systems balancing security and smart contract flexibility.  
  - **Tezos Etherlink**: Ground-up EVM implementation for compatibility edge cases.  
  - **Layer N (Rollup)**: Race conditions in high-performance parallel transaction systems.  
  - **Berachain (Beacon Kit)**: PoS economics and validator selection biases.  

- **Good Fit:**  
Expertise in parallel execution, EVM optimization, and consensus resilience, demonstrated through findings like cross-VM state inconsistencies and race conditions in high-performance systems, ensures thorough auditing of Monad's execution and database components.  

## SLIDE 2  

- **Auditing Methodology:**  
  -  **Architecture Analysis** - Review documentation, map execution paths, identify novel approaches and potential failure points  

  - **Threat Modeling** - Systematic analysis of attack vectors: economic attacks, consensus manipulation, state corruption, DoS vectors  

  - **Deep Code Analysis** - Line-by-line review of critical functions, custom testing frameworks, proof-of-concept exploits  

  - **Consensus & Economic Testing** - Model attack scenarios, analyze incentive structures, test edge cases in consensus logic  
  - **Documentation** - Detailed findings with technical analysis, exploitation steps, and remediation guidance  

- **Notable Findings:**  
  1. **Cosmos EVM (Cross-VM Inconsistency)**: State synchronization failures led to inconsistent state roots.  
  2. **Layer N (Race Condition)**: Parallel processing flaw allowed double-spends due to improper conflict detection.  
  3. **Tezos Etherlink (CALLCODE Bypass)**: Opcode filtering flaw enabled unlimited token minting.  
  4. **Berachain (Validator Bias)**: Staking mechanism manipulation skewed validator selection.  

- **Best-Fit Scopes:**  
  Execution Layer, MonadDB (TrieDB)  

- **Relevant Experience:**  
  - **Layer N**: Identified parallel execution race condition causing double-spends.  
  - **Filecoin**: Found custom EVM gas metering flaws leading to state inconsistency.  
  - **Cosmos EVM**: Detected cross-VM state sync failures causing inconsistent roots.  

---

# 0xdeadbeef  

## SLIDE 1  

- Specializes in auditing EVM based L1/L2 blockchains  
- Found more than 90 High & Medium vulnerabilities in Audit Contests  
- 10 Top-3 finishes in Audit contests  

- **Key Audits & Skills:**  
  - **Optimism, Blast, Base, Mantle**: Deep EVM compatibility analysis.  
  - **Filecoin, IOTA, Berachain**: Non-standard EVM re-implementations (opcodes, gas metering).  
  - **Private L1/L2 Audits**: Rust/Go-based clients under NDA.  

- **Good Fit:**  
Deep EVM expertise and ability to uncover chain-halting flaws, such as gas metering bugs and state divergence in parallel execution, make auditing of Monad's execution layer highly effective.  

## SLIDE 2  

- **Auditing Methodology:**  
  - Maps architecture via whitepapers and specs, focusing on consensus and execution deviations.  
  - Manually traces execution paths and state transitions, using IDE annotations for tracking.  
  - Runs local nodes and extends fuzzers to validate runtime behavior.  
  - Models attack surfaces (RPC, opcodes, block production) to identify critical inputs.  
  - Maintains structured logs of assumptions and gaps for documentation.  

- **Notable Findings:**  
  1. **EVM Compatibility Issue**: Identified opcode behavior inconsistency risking execution errors.  
  2. **Chain Stability Bug**: Detected issue causing potential chain halt in block production.  
  3. **RPC Interface Flaw**: Found crash vulnerability due to malformed input handling.  
  4. **Parallel Execution Error**: Uncovered state inconsistency under concurrent processing.  

- **Best-Fit Scopes:**  
  Execution Layer, Consensus  

- **Relevant Experience:**  
  - **Optimism, Blast, Base, Mantle**: Audited EVM execution and consensus optimizations.  
  - **Filecoin**: Identified high-severity flaws in Rust-based EVM implementation  

---

# mxuse  

## SLIDE 1  

- multiple top finishes on Sherlock  
- Top 25 on other platforms  
- Proven Bug Bounty Hunter, with several confirmed Critical and High Findings  
- **Key Audits & Skills:**  
  - **Omni Network**: Audited interoperability and shared security across chains, focusing on consensus and validator coordination.  
  - **Story Protocol**: Reviewed scalability and security at the blockchain layer.  
  - **Eigenlayer**: Analyzed restaking, slashing, and validator mechanisms.  
  - **Zetachain**: Identified critical bugs in mempool design, latency optimizations, and consensus security.  
  - **Immunefi**: Confirmed critical, high, and medium-severity findings in blockchain infrastructure protocols.  

- **C/C++ & Concurrency Expertise:**  
  - Proficient in analyzing BFT consensus and validator logic for concurrency and state consistency.  

- **Good Fit:**  
  Expertise in BFT consensus, validator coordination, and high-throughput systems, with proven ability to uncover critical chain-halting bugs, ensures rigorous analysis of consensus and execution components.  

## SLIDE 2  

- **Auditing Methodology:**  
  - Prioritizes validator logic, fund management, and chain-halting risks for deep system understanding.  
  - Maps execution flows from entry points using mind maps to trace data and logic propagation.  
  - Collects unusual code snippets in a dedicated folder for deeper investigation.  
  - Maintains bullet-point lists of areas to revisit and shares leads with co-auditors for feedback.  
  - Adapts approach based on protocol and client needs for optimal coverage.  

- **Notable Findings:**  
  1. **[Zetachain (Validator Quorum Flaw)](https://audits.sherlock.xyz/contests/857/voting/43)**: Static voter list in ballot threshold logic included tombstoned observers, causing inaccurate quorum evaluations.  
  2. **[Zetachain (Address Validation)](https://audits.sherlock.xyz/contests/857/voting/178)**: Unvalidated malformed address in Sui integration led to stuck withdrawals, DoS, and slashing risks.  
  3. **Immunefi (Blob Size DoS)**: Unchecked blob sizes from external data sources overwhelmed node execution, halting the network.  

- **Best-Fit Scopes:**  
  Consensus, Networking, Execution Layer  

- **Relevant Experience:**  
  - **Zetachain**: Uncovered quorum and validation flaws impacting consensus and transaction processing.  
  - **Immunefi**: Identified critical DoS vulnerability in blockchain infrastructure protocol.  

---

# Sammy  

## SLIDE 1  

- Blackthorn Founding Member  
- 7x top 2 in audit contests  
- specializing in Blockchain Infrastructure Audits  

- **Key Audits & Skills:**  
  - **Aleo (ZK L1)**: Memory bugs that could halt the chain.  
  - **Morph L2, Story Protocol (EVM L1/L2)**: Precompile gas models and execution layer security.  
  - **CosmWasm VM**: DoS and chain-split vulnerabilities due to non-determinism.  
  - **Brevis ZK Co-Processor, Irys (Data Chain)**: Rust-based systems and ZK infrastructure.  

- **Good Fit:**  
Ability to uncover chain-halting bugs in consensus, EVM, and ZK systems, including memory exhaustion and non-determinism issues, ensures comprehensive security for Monad's VM and execution components.  

## SLIDE 2  

- **Auditing Methodology:**  
  - Maps project-specific logic to identify unique attack surfaces.  
  - Skips boilerplate to focus on execution logic and cross-protocol integrations.  
  - Reproduces issues in live environments for validation.  
  - Combines immediate bug fixes with consolidated reports for critical vulnerabilities.  

- **Notable Findings:**  
  1. **Aleo (Memory Exhaustion)**: ZK bug allowed node crashes via unbounded memory allocation.  
  2. **[CosmWasm (Non-Determinism)](https://github.com/CosmWasm/cosmwasm/blob/main/SECURITY.md)**: Rust error caused chain splits due to inconsistent state transitions.  
  3. **Story Protocol (Gas Miscalculation)**: Underpriced precompiles enabled cheap DoS attacks.  

- **Best-Fit Scopes:**  
  Compiler & VM (MonadVM), Execution Layer  

- **Relevant Experience:**  
  - **CosmWasm VM**: Found non-deterministic Rust error causing chain splits and exposed VM entry point leading to unexpected contract behavior.  
  - **Story Protocol**: Detected gas miscalculations in precompiles enabling DoS.  

# Guido Vranken  

## SLIDE 1  

- No. 1 on Ethereum’s Bug Bounty Leaderboard  
- Expert in Cybersecurity and Blockchain technology  

- **Key Audits & Skills:**  
  - **REVM (Rust)**: Audited Rust-based EVM implementation, focusing on execution logic and gas metering.  
  - **OpenVPN (C)**: Identified critical flaws in C-based system.  
  - **EOS (C++)**: Uncovered high-severity bugs, including memory corruption.  
  - **Cryptographic Libraries**: Found 40+ critical bugs in OpenSSL, LibreSSL, BoringSSL (memory leaks, OOB reads/writes, non-determinism).  
  - **CosmWasm VM & Brevis ZK Co-Processor (Rust)**: Focused on VM security and ZK proof verification.  

- **C/C++ & Concurrency Expertise:**  
  - Proficient in C/C++ memory safety, identifying critical flaws in OpenVPN and EOS.  

- **Good Fit:**  
  Expertise in cryptographic security, low-level C/C++ systems, and EVM/VM auditing, with proven ability to detect memory corruption and non-determinism, ensures rigorous analysis of execution, VM, and consensus components.  

## SLIDE 2  

- **Auditing Methodology:**  
  - Maps protocol goals to identify novel attack surfaces.  
  - Prioritizes validator logic, slashing conditions, and chain-halting risks.  
  - Reproduces bugs locally for validation (e.g., gas miscalculations, memory exhaustion).  
  - Consolidates findings into actionable reports with exploit steps and mitigations.  

- **Notable Findings:**  
  1. **[OpenSSL (Memory Leak/DoS)](https://www.openssl.org/news/secadv/20220913.txt)**: ARIA GCM ciphers leaked memory via `EVP_CTRL_AEAD_SET_IVLEN`, risking DoS.  
  2. **[EOS (C++ Memory Corruption)](https://www.businessinsider.nl/blockone-pays-hacker-120000-to-expose-flaws-in-eos-source-code-ahead-of-blockchain-launch-2018-6/)**: Malformed transactions caused node crashes via buffer overflows.  
  3. **[CosmWasm VM (Non-Determinism)](https://github.com/CosmWasm/cosmwasm/blob/main/SECURITY.md)**: Exposed entry point led to inconsistent state transitions.  

- **Best-Fit Scopes:**  
  Execution Layer, Compiler & VM, Networking  

- **Relevant Experience:**  
  - **REVM**: Audited execution logic and gas metering in Rust-based EVM.  
  - **[EOS](https://www.businessinsider.nl/blockone-pays-hacker-120000-to-expose-flaws-in-eos-source-code-ahead-of-blockchain-launch-2018-6/)**: Identified memory corruption vulnerabilities in C++ blockchain system.  
  - **[CosmWasm VM](https://github.com/CosmWasm/cosmwasm/blob/main/SECURITY.md)**: Detected non-determinism issues impacting state consistency.  

# David Theodore  

## SLIDE 1  

- [Co-authored](https://arxiv.org/pdf/2402.15293.pdf) seminal ZK security paper  
- **Key Audits & Skills:**  
  - **Ethereum Foundation (Geth/Prysm)**: Fuzzed and audited Go-based Ethereum clients for panics, crashes, and consensus edge cases.  
  - **Spearbit Audits (EigenDA, Blast, Overprotocol)**: Reviewed data availability systems and L2 infrastructure; served as Go judge for Blast’s Cantina competition.  
  - **Aleo snarkVM (Rust)**: Audited ZK virtual machine, uncovering critical bugs.  
  - **Fuzzing Innovation**: Developed [tool](https://www.youtube.com/watch?v=GrppANUs8zM) using Go’s AST parser to auto-generate fuzz harnesses for large-scale bug detection.  
  - **System-Level Proficiency**: Experienced in Rust/C/C++ for low-level security audits (memory safety, concurrency).  

- **C/C++ & Concurrency Expertise:**  
  - Proficient in Rust/C/C++ for memory safety and concurrency in low-level systems.  

- **Good Fit:**  
  Expertise in ZK security, Go/Rust auditing, and fuzzing, with proven ability to uncover panics and memory exhaustion, ensures rigorous analysis of execution, VM, and consensus components.  

## SLIDE 2  

- **Auditing Methodology:**  
  - Uses custom AST parser to generate fuzz targets for crash/DoS detection.  
  - Reviews critical paths (validator logic, slashing, state transitions) for logic flaws.  
  - Combines static analysis, dynamic testing, and PoC exploits for validation.  
  - Builds audit teams to cross-verify findings.  

- **Notable Findings:**  
  1. **Aleo snarkVM (Memory Exhaustion)**: ZK proof generation exploited unbounded memory allocation, crashing nodes.  
  2. **Spearbit Audits (EigenDA, Blast, Overprotocol)**: Identified high-severity bugs in data availability and L2 systems.  

- **Best-Fit Scopes:**  
  Execution Layer, Compiler & VM, Data Availability  

- **Relevant Experience:**  
  - **Aleo snarkVM**: Uncovered memory exhaustion bugs in Rust-based ZK VM.  
  - **Ethereum Foundation (Geth/Prysm)**: Detected panics and consensus edge cases in Go clients.  
  - **Spearbit (Blast)**: Audited L2 scaling solution and judged Go-based competition.  

# Berndartmueller

## SLIDE 1

- **Key Audits & Skills:**  
  - **Initia Cosmos SDK Rollup (Go):** Audited custom EVM compatibility module and rollup framework.  
  - **Filecoin FEVM (Rust):** Audited custom EVM implementation.  
  - **IOTA ISC (Rust):** Audited EVM contracts and consensus mechanism.  
  - **Irys datachain with EVM (Rust):** Audited custom L1 with EVM compatibility and consensus.  
  - **Ronin/Sky Mavis (Go):** Audited delegated PoS with custom consensus.  

- **Go & Rust Expertise:**  
  - Proficient in auditing blockchain systems implemented in Go and Rust, with a focus on custom EVM integrations and consensus mechanisms.  

- **Good Fit:**  
  - Expertise in auditing custom EVM implementations and consensus mechanisms, combined with proficiency in Go and Rust, ensures thorough evaluation of execution and consensus components.  

## SLIDE 2

- **Auditing Methodology:**  
  - Reviews documentation, whitepapers, and design documents to gain a high-level understanding of the protocol.  
  - Traces code from main user entry points to identify key components and their interactions.  
  - Adopts an initial "tourist" approach to explore critical areas, noting potential issues, followed by a detailed line-by-line review with a focus on user inputs.  
  - Uses audit tags (e.g., `@follow-up`, `@note`) in the code and maintains detailed notes in Markdown files.  
  - Creates mind maps and diagrams to visualize user flows and complex interactions.  
  - Examines test suites and coverage to uncover edge cases and confirm expected protocol behavior.  

- **Notable Findings:**  
  1. **Initia Cosmos SDK Rollup (Message Disguise):** Identified that a Cosmos SDK message disguised as an EVM transaction caused `ListenFinalizeBlock` errors, halting block indexing.  
  2. **Initia Cosmos SDK Rollup (Gas Cost Flaw):** Discovered missing intrinsic gas charges for EVM transactions, enabling resource abuse via access list manipulation.  
  3. **Filecoin FEVM (Gas Charging Issues):** Found that inadequate gas charging allowed resource exhaustion, threatening block production and chain stability.  

- **Best-Fit Scopes:**  
  - Execution Layer, Consensus  

- **Relevant Experience:**  
  - **Initia Cosmos SDK Rollup:** Uncovered critical vulnerabilities in custom EVM integration, including message handling and gas cost enforcement.  
  - **Filecoin FEVM:** Detected gas charging flaws in a Rust-based EVM implementation that risked chain performance.  
  - **IOTA ISC:** Audited EVM contracts and consensus, identifying transaction processing vulnerabilities (e.g., mempool bypass impacting user transactions).  



### One-Slide Descriptions

#### deadbeef
- **Key Audits & Skills**: Audited EVM-compatible L1/L2 chains (Optimism, Blast, Base, Mantle, Filecoin), specializing in execution and consensus optimizations.  
- **C/C++ & Concurrency Expertise**: Proficient in auditing C/C++ for memory safety and Rust/Go for execution integrity.  
- **Notable Findings**: Discovered critical EVM compatibility issues and chain stability bugs, such as opcode inconsistencies and potential chain halts.  
- **Fit for Scopes**: Perfect for auditing Monad’s Execution Layer and Consensus, leveraging deep EVM expertise and experience with non-standard implementations to ensure robust transaction processing and block production analysis.

#### mxuse
- **Key Audits & Skills**: Audited blockchain infrastructure protocols (Omni Network, Story Protocol, Eigenlayer, Zetachain), focusing on consensus and validator coordination.  
- **C/C++ & Concurrency Expertise**: Skilled in analyzing BFT consensus and validator logic for concurrency and state consistency.  
- **Notable Findings**: Identified critical vulnerabilities like validator quorum flaws and blob size DoS attacks, showcasing ability to uncover chain-halting issues.  
- **Fit for Scopes**: Well-suited for Consensus, Networking, and Execution Layer audits, with proven expertise in high-throughput systems and BFT consensus to thoroughly evaluate validator dynamics and network resilience.

### Why They Are a Good Fit

#### Why deadbeef is a good fit
deadbeef is perfect for auditing Monad’s Execution Layer and Consensus due to deep expertise in EVM-compatible L1/L2 chains and non-standard implementations. Experience with chains like Optimism, Blast, and Filecoin ensures robust analysis of transaction processing, block production, and consensus optimizations.

#### Why mxuse is a good fit
mxuse is well-suited for auditing Monad’s Consensus, Networking, and Execution Layer, leveraging proven expertise in BFT consensus, validator coordination, and high-throughput systems. Experience with protocols like Omni Network and Zetachain ensures thorough evaluation of validator dynamics, network resilience, and chain-halting risks.

---