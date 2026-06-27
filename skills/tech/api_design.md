# tech/api_design.md
Skill ID: tech-api-design-04
Category: Technology
Agent: T-01, MGR-TECH
Difficulty: Advanced

## Definition
Designing robust, scalable, maintainable API contracts between services that enable independent development and clear integration patterns.

## Principles
1. **Consistency**: Same patterns across all endpoints
2. **Versioning**: URL path or header version, never break existing
3. **Backward compatibility**: Additive changes only
4. **Statelessness**: No server-side session state
5. **Idempotency**: POST retries don't create duplicates

## REST Best Practices
- Resources, not actions: `/users` not `/getUser`
- Plural nouns for collections
- Nesting max 1 level deep
- Standard status codes (200, 201, 400, 401, 403, 404, 429, 500)
- Pagination always for collections
- Filtering via query params

## Error Response Format
```
{
  "error": {
    "code": "VALIDATION_FAILED",
    "message": "Human-readable description",
    "field": "email",
    "docs_url": "https://docs.example.com/errors#VALIDATION_FAILED"
  }
}
```

## Rate Limiting
- Default: 100 req/min per API key
- Headers: `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `Retry-After`
- 429 response with Retry-After header

## KPIs
- API uptime: 99.9%
- P99 latency: < 500ms
- Error rate: < 0.1%
- Breaking changes per quarter: 0
