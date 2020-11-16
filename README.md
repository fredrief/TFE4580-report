TFE4580 Project report
# Control-Bounded Conversion for ultrasound applications

#### Main goal of report:
- Give the reader a thorough understanding of the control-bounded conversion principle, its relation to $\Sigma\Delta$ converters and the relevant ADC architectures introduced by Malmberg
- Present theoretical analysis of SNR improvement by using multi-input Hadamard ADC, based on raw data GE
- Demonstrate simulations (at least with CIADC)
- Present developed python simulation framework

#### Report structure
1. Introduction
   1. Background
   2. Motivation
   3. Report outline
2. Theoretical background
   1. AD Conversion basics. Limitation of sample centric conversion
   2. Conventional oversampling conversion
   3. Control-Bounded conversion.
      1. Principle of operation
      2. Conceptual relation to $\Sigma\Delta$
      3. Brief derivation of performance measures
3. ADC architectures
   1. Chain-of-integrators ADC
      1. Analog system
         -  Transfer functions and state space matrices
      2. Local digital control
         - Criteria for effective control
      3. Digital estimator
      4. Briefly mentioning leapfrog extension (complex poles)
   2. Hadamard ADC
      1. State space matrices (rotated)
      2. Digital control
      3. Digital estimator
         - Essentially no different from CIADC
      4. Over/undercompleteness
      5. Multiple input
         -  SNR gain from having multiple inputs
4. Multi-input ADC for ultra sound (What gain could we expect)
   1. Assumptions and method
   2. Results
5. Implementation and simulation
   1. CIADC
      1. Derivation of desired parameters with multiple input US application in mind
      2. Simulation results for CIADC
   2. HCI and multiple input if applicable
6. Python framework
7. Conclusions and outlook
