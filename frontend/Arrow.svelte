<script lang="ts">
    export let width = '16px';
    export let height = '16px';
    export let direction: string = "asc";
</script>

<svg
    class="svg-arrow {$$props.class} "
    class:down={direction === "desc"}
    {width}
    {height}
    xmlns="http://www.w3.org/2000/svg"
    viewBox="0 0 100 100"
    on:click
    on:keypress
    aria-roledescription="Sorts table in {direction}ending order"
    role="button"
    tabindex="0"
>
    <polygon points="50 15, 100 80, 0 80" />
</svg>


<style>
.down {
    rotate: 180deg;
}

.svg-arrow {
	display: inline-block;
	fill: var(--body-text-color);
    transition-property: fill;
    transition-duration: 0.25s;
    transition-timing-function: ease-in-out;
}

.svg-arrow:hover {
    fill: magenta;
    cursor: pointer;
}
</style>