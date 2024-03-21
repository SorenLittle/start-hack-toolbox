

## Setup

### Environment Variables

| Variable | Default | Purpose |
|----------|---------|---------|
| MONGO_DB     | start-hack  | Name of the target database in MongoDB |

### F/E Setup

Open css auto-refresh in a parallel terminal

```bash
cd src/app/frontend/static
npm run build
```

There is a helpful pink outline applied to the base layer css for debugging purposes. To remove it, comment out the following line in [`input.css`](src/app/frontend/static/css/input.css):

```css
@layer base {
    * {
        @apply outline outline-1 outline-pink-200 
    }
    
    /* ... */
}
```