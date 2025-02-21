This is the start of an algorithm to zipper multiple proposer's txs.

Users pay for inclusion to any/all validators. The validator includes then orders based on Fee/CU. That's it, they don't pack into threads or execute because the final block will be zippered.

Each proposer sends their ordered list of txs **and** an array of accounts that overlap.

Each proposer takes the other proposers' array of overlapping sets, and merges the sets to have a complete view of the overlapping sets.

They then take the ordered lists of txs from each proposer. They pop off the highest Fee/CU tx, map it to the overlapping set.

There are many easy way to take this overlapping set and deterministically make a mapping to a thread for processing.

TODO:
- What is the deterministic mapping from proposers to threads?
- - Ordering the sets and snaking them across threads should be ok, but not optimal.
- can you use the total CU of the overlapping set?

```mermaid
graph TD;
    %% Users pay for inclusion
    A["Users pay for inclusion"] --> P1["Proposer 1"];
    A --> P2["Proposer 2"];
    A --> P3["Proposer 3"];
    A --> P4["Proposer 4"];

    %% Each proposer orders transactions independently
    P1 --> O1["Ordered list (P1)"];
    P2 --> O2["Ordered list (P2)"];
    P3 --> O3["Ordered list (P3)"];
    P4 --> O4["Ordered list (P4)"];

    %% Proposers send ordered lists & overlapping sets
    O1 --> M["Merge overlapping sets (each proposer"];
    O2 --> M;
    O3 --> M;
    O4 --> M;

    %% Merging overlapping sets to determine thread mapping
    M --> F["Pop highest Fee/CU tx"];
    F --> G["Assign to a processing thread"];

    %% Final processing and execution
    G --> H["Thread assignment for execution"];
    H --> I["Final ordered block"];

    %% Styling
    classDef yellow fill:#ffcc00,stroke:#333,stroke-width:2px;
    classDef orange fill:#ff9966,stroke:#333,stroke-width:2px;
    classDef blue fill:#66ccff,stroke:#333,stroke-width:2px;
    classDef green fill:#99cc99,stroke:#333,stroke-width:2px;

    class A,I yellow;
    class P1,P2,P3,P4,O1,O2,O3,O4 orange;
    class M blue;
    class F,G,H green;
```

 