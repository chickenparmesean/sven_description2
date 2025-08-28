## Gabriel Jaldon  

- **Audit Leadership**: Led 10+ high-stakes audits, uncovering 50+ critical vulnerabilities across Cosmos, Solana, and EVM ecosystems.  
- **Contest Success**: Won all **Rust contests** and **Cosmos-SDK Go contests** they participated on Sherlock, ranking in Top 15 ELO.  
- **Cross-Chain Expertise**: Audited 5+ cross-chain protocols, including Zetachain’s *tss-lib* fork, securing $1B+ in TVL.  

**Key Audits & Skills**:  
- **Zetachain** (CosmosSDK, Cross-Chain): Led Sherlock’s audit, identifying 13 High & 3 Medium severity issues, including vulnerabilities in their forked *tss-lib* (GG20 Threshold Signature Scheme).  
- **IOTA Chain & L2** (Rust, Go, Move): Audited MoveVM integration and off-chain Go components for the L2 Rebase project, mitigating multi-chain operational risks.  
- **Seda Protocol** (Cosmos SDK, BFT): Uncovered critical flaws in cross-chain validator consensus and governance mechanisms.  
- **GETH Forks & Optimism L2** (EVM): Audited custom EVM implementations for Layer 2 scaling, including forked GETH infrastructure.  

**VM & Cross-Chain Expertise**:  
- **tss-lib Familiarity**: Audited Zetachain’s forked *tss-lib* (GG20), enabling thorough validation of threshold signature workflows.  
- **VM Integrations**: Secured IOTA’s MoveVM and Sui integrations, addressing UTXO/EVM/BFT interoperability challenges.  

**Auditing Methodology**:  
- Reviews documentation, whitepapers, and design documents to gain high-level protocol understanding.
- Traces code from main user entry points to identify critical components and interactions.
- Uses audit tags (e.g., @follow-up, @note) in code and maintains detailed notes in Markdown.
- Creates mind maps and diagrams to visualize user flows and complex interactions.
- Examines test suites and coverage to uncover edge cases and confirm protocol behavior.


**Relevant Qualifications**:  
Gabriel’s CosmosSDK/Go and Crosschain experience, combined with *tss-lib* experience, ensures robust validation of ThorChain’s GG20 TSS and hybrid architecture. 

## Berndartmueller  

- **Audit Impact**: Secured 15+ protocols, identifying 40+ high-severity issues across Cosmos, EVM, and Rust-based chains.  
- **Contest Achievements**: **1st-place in ZetaChain C4 contest**, Top50 Sherlock ELO, with $500K+ in bug bounties earned.  
- **Multi-Chain Proficiency**: Audited 10+ multi-chain systems, securing validator and cross-chain logic for $2B+ TVL.  

**Key Audits & Skills**:  
- **ZetaChain** (CosmosSDK, Cross-Chain): Secured multiple audits, achieving **1st-place in their C4 contest**, identifying critical issues in cross-chain message handling.  
- **Initia Cosmos SDK Rollup** (Go): Detected gas cost enforcement flaws and EVM transaction disguising as Cosmos messages, impacting block stability.  
- **IOTA ISC** (Rust, EVM): Led Sherlock’s audit of EVM contracts and consensus mechanisms, addressing transaction processing gaps.  
- **Ronin/Sky Mavis** (Go, Delegated PoS): Reviewed validator dynamics and custom consensus in a Cosmos-based PoS system.  
- **Irys Datachain** (Rust, EVM): Audited a custom L1 with EVM compatibility, focusing on multi-chain consensus risks.  

**Notable Vulnerabilities Identified**:  
- **Initia Cosmos SDK** (Message Disguise): EVM transactions masquerading as Cosmos messages caused `ListenFinalizeBlock` errors, halting indexing.  
- **Initia Cosmos SDK** (Gas Cost Flaw): Missing intrinsic gas charges for EVM transactions allowed resource abuse via access list manipulation.  

**Auditing Methodology**:  
- **Documentation & Code Tracing**: Reviews whitepapers and traces code from user entry points to map critical logic.  
- **Tourist Approach**: Prioritizes high-risk areas, followed by line-by-line analysis with tags (`@follow-up`, `@note`).  
- **Visualization**: Uses mind maps and flow diagrams to identify edge cases in cross-chain interactions.  
- **Test Suite Validation**: Examines coverage to stress-test consensus edge cases (e.g., validator stalls, chain-specific logic).  

**Relevant Qualifications**:  
Berndartmueller’s multiple years of CosmosSDK/Go auditing and experience with projects similiar to Thorchain ensure a robust security analasyis of Thorchains PRs. His multi-chain expertise (EVM, SUI, Solana) supports cross-chain dependency validation.  


## Sammy  

- **Audit Track Record**: Secured 12+ protocols, uncovering 30+ critical bugs in Cosmos, ZK, and EVM-based systems.  
- **Contest Performer**: **1st-place in Story Protocol 2024 contest**, with **3 wins and 7 top-2 finishes** in 2024.  
- **Cross-chain & DeFi Expertise**: Audited 5+ Cross-chain and DeFi protocols, securing $1.5B+ in TVL.  

**Key Audits & Skills**:  
- **Story Protocol** (CosmosSDK, EVM L2): Achieved **1st-place the contest**, identifying gas miscalculations in precompiles enabling low-cost DoS attacks.  
- **CosmWasm VM** (Rust, Go): Detected non-deterministic behavior in Rust-based contract execution, leading to chain splits and validator conflicts.  
- **Aleo snarkVM** (zkVM): Uncovered **2+ critical issues**, including a delegation-related DoS vulnerability causing node crashes and consensus stalls in ZK-based systems.  
- **LayerZero, Beraborrow** (Solidity, EVM): Validated cross-chain bridge logic and governance edge cases in EVM-based lending protocols.  

**Technical Expertise**:  
- **CosmosSDK/Go**: Audited Story Protocol’s EVM L1 and CosmWasm VM codebases, relevant to ThorChain’s hybrid architecture.  
- **L1 and L2 solutuions**: Specializes in execution layer security (Morph L2, Aleo ZK L1), addressing cross-chain scaling challenges.  
- **Smart Contract VMs**: Proficient in CosmWasm (Rust), Solidity (EVM), and ZK VMs (Aleo, Brevis), supporting ECDSA/EDDSA and GG20 Threshold Signature Scheme validation.  

**Notable Findings**:  
- **Story Protocol** (Gas Miscalculation): Exposed underpriced precompiles enabling low-cost DoS attacks on EVM execution layer.  
- **EigenLayer** (PoS Infrastructure): Validator slashing gaps allowing offline staking rewards

**Auditing Methodology**:  
- Architecture Analysis: Reviews documentation, whitepapers, and design documents to map project-specific logic.
- Threat Modeling: Prioritizes attack surfaces unique to the protocol (e.g., cross-chain messaging, gas models).
- Deep Code Analysis: Skips boilerplate code to focus on execution logic and cross-protocol integrations.
- Documentation: Combines immediate mitigation steps (e.g., "fix reentrancy in flashLoan") with consolidated reports for critical vulnerabilities (e.g., Story Protocol gas flaws).


**Relevant Qualifications**:  
Sammy’s CosmosSDK/Go expertise and cryptography experience, with Story Protocol and CosmWasm VM audits, makes them a perfect fit for state machine and cryptographic component validation. His EVM and chain-splitting flaw experience ensures robust cross-chain security.  


## Kuprum  

- **Cosmos Experience**: Conducted 10+ audits at Informal Systems, securing $3B+ in Cosmos ecosystem TVL.  
- **Contest Performer**: **Top 5 performer on other platforms**, with 20+ high-severity findings across IBC and EVM protocols.  
- **Crosschain Communication**: Audited 5+ IBC implementations, mitigating consensus and cross-chain risks.  

**Key Audits & Skills**:  
- **IBC & IBC V2** (Cosmos - Inter-Blockchain Communication): Conducted core IBC protocol audits, identifying consensus and state transition vulnerabilities.  
- **CosmosEVM** (EVM on Cosmos): Audited EVM implementations within Cosmos, focusing on precompile gas models and execution layer risks.  
- **Story Protocol** (CosmosSDK L1): Secured 2 findings in 2024, including gas miscalculations and consensus edge cases in their CosmosSDK fork.  
- **Omni Network** (Rollup Interoperability): Identified critical and medium-severity vulnerabilities, including challenge period bypasses and LPP metadata tampering risks in Optimism Superchain integration.  
- **Lombard** (IBC V2 Integration): Led audit of IBC V2, exposing vault licensing design flaws leading to collateral double-counting and asset freezing.  

**Go & IBC Expertise**:  
- **Cosmos SDK/Go Specialist**: Conducted 10+ audits at Informal Systems, covering validator dynamics, staking logic, and IBC packet handling.  
- **Cross-Chain Protocol Depth**: Experience with **Omni Network** (rollup bridging), **Lombard** (IBC V2), and **DYAD** (vault licensing), supporting UTXO/EVM/BFT dependency analysis.  


**Relevant Qualifications**:  
Kuprum’s 5+ years of Cosmos/IBC expertise and Go proficiency ensure thorough ThorChain validator and cross-chain logic validation. His IBC V2 and EVM audit experience supports multi-chain dependency security.  

## Hack3r-0m  

- **Audit Contributions**: Secured 10+ Cosmos and EVM protocols, uncovering 25+ high-severity vulnerabilities.  
- **Contest Performance**: **Code4rena Top 20 performer**, with 9+ critical findings in staking and cross-chain systems.  
- **Consensus Focus**: Audited 5+ consensus mechanisms, mitigating slashing and incentive risks.  

**Key Audits & Skills**:  
- **Cosmos IBC Eureka** (IBC Protocol): Participated in Interchain Labs’ audit, focusing on cross-chain message ordering, validator health checks, and IBC packet replay vulnerabilities.  
- **Ethereum Pectra Upgrade** (Cryptography, Consensus): Audited core protocol changes for Ethereum’s Pectra hard fork, including withdrawal credentials and validator slashing conditions.  
- **EigenLayer** (Consensus, Game Theory): Uncovered 4+ high-severity issues in staking and slashing mechanisms, preventing incentive misalignments.  
- **Berachain** (CosmWasm, EVM): Audited hybrid EVM/CosmWasm integrations, addressing state bloat and reentrancy risks.  
- **dYdX v4, Noble, Osmosis** (Cosmos SDK): Audited validator delegation, staking rewards, and chain governance logic in high-traffic Cosmos networks.  

**Technical Expertise**:  
- **Cosmos SDK/Go**: 1.2+ years of experience with IBC, ABCI, and Tendermint/CometBFT, supporting validator and node security reviews.  
- **Cryptography**: Proficient in auditing CosmWasm and TEE-based systems, and experience in cryptograhy. 
- **Cross-Chain Experience**: Audited **EigenLayer** (staking), **Rio Network** (cross-chain lending), and **LayerZero** (bridging) for high-severity bugs.  

**Auditing Methodology**:  
- Focuses on user flow tracing from frontend to protocol logic.
- Applies contest-grade scrutiny to DeFi and cross-chain logic (e.g., reentrancy, slippage).
- Reproduces exploits in testnet environments to confirm attack viability.
- Maintains direct communication with teams for actionable remediation (e.g., Sherlock collabs).


**Relevant Qualifications**:  
Hack3r-0m’s Cosmos SDK/IBC and consensus expertise, with EVM/UTXO experience, supports ThorChain’s validator and cross-chain security. His high-impact findings ensure protocol seucrity.  


## KupiaSec  

- **THORChain Experience**: Audited THORWallet, securing user asset flows with 1 High and 1 Medium finding.  
- **Contest Leadership**: **1st-place in 8+ Sherlock/Code4rena contests**, with 12+ top-tier finishes.  
- **DeFi & Cross-Chain**: Secured 10+ DeFi and cross-chain protocols, protecting $1B+ in TVL.  

**Key Audits & Skills**:  
- **THORWallet** (Cosmos Ecosystem, Wallet Security): Identified 1 High and 1 Medium-severity vulnerability in THORChain’s wallet-layer logic, addressing user asset flows and protocol integration risks.  
- **EVM & Cosmos Application Security**: Audited **Uniswap Swap Router** (EVM), **RootsFi** (Cross-Chain), and **Lazy Bear** (DeFi) for transaction flow and frontend logic risks.  
- **DeFi & Cross-Chain Expertise**: Secured 1st-place finishes in **Sherlock** contests (FlatMoney v2, Usual Protocol) and **Code4rena** (ULTI, Doubler Mitigation), focusing on AMM, lending, and cross-chain messaging.  

**Technical Expertise**:  
- **Wallet & Frontend Security**: Audited THORChain-integrated wallets before, ensuring secure transaction handling and asset flow validation.  
- **Multi-Chain Application Review**: Experience with **EVM** (Uniswap, FlatMoney), **Cosmos** (RootsFi), and **Solana** (Rain, GMX) protocols.  


**Relevant Qualifications**:  
KupiaSec’s THORWallet audit experience and DeFi/cross-chain expertise ensure robust ThorChain user asset flow and multi-chain integration security. His contest success validates high-stakes protocol analysis.  


## DefSec  

- **Audit Scale**: Secured 15+ protocols, with **90+ high-severity findings** across Cosmos, EVM, and cross-chain systems.  
- **Contest Ranking**: **Top50 Code4rena**, with 12+ top-tier contest placements securing $2B+ TVL.  
- **VM & Consensus Expertise**: Audited 8+ VM and consensus mechanisms, mitigating state and economic risks.  

**Key Audits & Skills**:  
- **Cosmos EVM & CosmWasmVM** (Cross-VM Validation): Uncovered low/medium-severity issues in **state synchronization** and **parallel execution** flaws across hybrid Cosmos VMs.  
- **Layer N** (Parallel Rollup): Exposed race conditions in **high-performance transaction systems**, enabling double-spends due to improper conflict detection.  
- **LayerZero** (Cross-Chain Interoperability): Audited omnichain messaging protocol for **message replay** and **validator collusion risks**.  
- **Injective, Mantra Chain, Entangle** (Cosmos DeFi Hubs): Secured **validator economics**, **yield aggregation**, and **cross-chain liquidity** mechanisms.  
- **Tezos Etherlink, Aurora** (EVM-Compatible L2s): Audited for compatibility edge cases.
- **Core Chain (Bitcoin L1), Gravity Bridge** (EVM-Cosmos Bridge): Reviewed hybrid consensus for **smart contract flexibility** and **peg security** in Bitcoin-based systems.  

**Technical Expertise**:  
- **VM Architecture**: Specializes in **parallel execution**, **opcode filtering**, and **module isolation** in EVM forks (e.g., Etherlink, Aurora).  
- **Consensus & Economic Modeling**: Proven in **PoS staking biases** (Berachain), **validator selection flaws** (Mantra Chain), and **race condition exploitation** (Layer N).  
- **Cross-Chain Security**: Experience with **LayerZero** and **Gravity Bridge**, supporting external chain dependency analysis.  

**Notable Vulnerabilities Identified**:  
1. **Cosmos EVM** (State Sync Failure): Cross-VM state inconsistencies led to **divergent state roots** in parallel execution.  
2. **Layer N** (Double-Spend Vector): Race condition allowed **conflict detection bypass**, enabling transaction replay attacks.  
3. **Tezos Etherlink** (CALLCODE Exploit): Opcode filtering flaw permitted **unlimited token minting** via EVM compatibility layer.  
4. **Berachain** (Validator Bias): Staking mechanics manipulation skewed **validator selection** toward large delegators.  

**Auditing Methodology**:  
- **Architecture Deep-Dive**: Maps execution paths from user flows to VM internals, prioritizing **state consistency** and **consensus edge cases**.  
- **Threat Modeling**: Analyzes **economic attack vectors** (e.g., validator collusion), **DoS risks**, and **state corruption** in multi-chain systems.  
- **Line-by-Line Code Review**: Focuses on **critical functions** (e.g., TSS entropy checks, EVM precompile validation) with custom testing frameworks.  
- **Consensus Stress-Testing**: Simulates Byzantine validator behavior and **incentive misalignments** in staking protocols.  
- **Remediation Documentation**: Provides **exploitation steps**, **attack impact assessments**, and **actionable fix guidance** in audit reports.  

**Relevant Qualifications**:  
DefSec’s cross-VM and consensus expertise, with LayerZero/Gravity Bridge audits, ensures ThorChain’s multi-chain and validator security. His 90+ high-severity findings validate robust risk detection.  


---