# tech/testing_strategies.md
Skill ID: tech-testing-07
Category: Technology
Agent: T-01, MGR-TECH
Difficulty: Advanced

## Definition
Systematic approach to verifying software correctness, performance, and reliability through multiple test layers.

## Test Pyramid
```
        /\
       /UI\        ← 10% E2E / UI tests (slow, expensive)
      /----\
     /SERVIC\      ← 20% Integration tests
    /--------\
   /UNIT TESTS\   ← 70% Unit tests (fast, cheap)
  /------------\
```

## Test Types
1. **Unit**: Single function/method, no external deps
2. **Integration**: 2+ components together (API + DB)
3. **E2E**: Full user journey through UI
4. **Performance**: Load, stress, spike testing
5. **Chaos**: Inject failures, verify resilience
6. **Smoke**: After deploy, basic health checks

## Quality Gates
- Unit test coverage: 80%+ for new code
- All tests pass before merge
- E2E critical paths green before deploy
- Performance regression: < 10% degradation

## When to Skip Tests
- Pure configuration change (with review)
- Documentation fix
- Trivial typo in non-logic code

## KPIs
- Test coverage: 80%+
- Flaky test rate: < 2%
- Bugs caught pre-production: 90%+
- Test execution time: < 10 min for unit suite
